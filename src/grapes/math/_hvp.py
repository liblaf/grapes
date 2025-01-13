from collections.abc import Callable
from typing import Literal

import jax
import jax.numpy as jnp


def hvp(
    fun: Callable,
    x: jax.Array,
    v: jax.Array,
    *,
    method: Literal[
        "grad-of-grad",
        "forward-over-reverse",
        "reverse-over-forward",
        "reverse-over-reverse",
    ] = "forward-over-reverse",
) -> jax.Array:
    """Hessian-vector products.

    References:
        [1] [The Autodiff Cookbook — JAX documentation](https://jax.readthedocs.io/en/latest/notebooks/autodiff_cookbook.html)
    """
    match method:
        case "grad-of-grad":
            return jax.grad(lambda x: jnp.vdot(jax.grad(fun)(x), v))(x)
        case "forward-over-reverse":
            return jax.jvp(jax.grad(fun), (x,), (v,))[1]
        case "reverse-over-forward":
            g = lambda primals: jax.jvp(fun, primals, (v,))[1]  # noqa: E731
            return jax.grad(g)((x,))
        case "reverse-over-reverse":
            return jax.grad(lambda x: jnp.vdot(jax.grad(fun)(x), v))(x)
        case _:
            msg = f"Unknown method '{method}' for Hessians-vector products"
            raise ValueError(msg)
