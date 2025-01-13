import abc
import functools
from collections.abc import Callable

import jax
import jax.numpy as jnp
import numpy.typing as npt
from jaxtyping import Float

import grapes as gr


class Problem(abc.ABC):
    p: jax.Array  # material properties
    s: jax.Array  # state variables

    def reload(self, p: Float[npt.ArrayLike, "..."]) -> None:
        p = jnp.asarray(p)
        s: Float[jax.Array, " ..."] = self._reload(p)
        self.p = p
        self.s = s

    def fun(
        self,
        u: Float[npt.ArrayLike, " DoF"],
        p: Float[npt.ArrayLike, "..."] | None = None,
        s: Float[npt.ArrayLike, "..."] | None = None,
    ) -> Float[jax.Array, ""]:
        p, s = self._prepare_p_s(p, s)
        return self._fun_jit(jnp.asarray(u), jnp.asarray(p), jnp.asarray(s))

    def jac(
        self,
        u: Float[npt.ArrayLike, " DoF"],
        p: Float[npt.ArrayLike, "..."] | None = None,
        s: Float[npt.ArrayLike, "..."] | None = None,
    ) -> Float[jax.Array, " DoF"]:
        if s is None:
            s = self.s
        if p is None:
            p = self.p
        return self._jac_jit(jnp.asarray(u), jnp.asarray(s), jnp.asarray(p))

    def hess(
        self,
        u: Float[npt.ArrayLike, " DoF"],
        p: Float[npt.ArrayLike, "..."] | None = None,
        s: Float[npt.ArrayLike, "..."] | None = None,
    ) -> Float[jax.Array, " DoF DoF"]:
        # TODO: Implement hessian
        raise NotImplementedError

    def hessp(
        self,
        u: Float[npt.ArrayLike, " DoF"],
        v: Float[npt.ArrayLike, " DoF"],
        p: Float[npt.ArrayLike, "..."] | None = None,
        s: Float[npt.ArrayLike, "..."] | None = None,
    ) -> Float[jax.Array, " DoF"]:
        p, s = self._prepare_p_s(p, s)
        return self._hessp(
            jnp.asarray(u), jnp.asarray(v), jnp.asarray(p), jnp.asarray(s)
        )

    def _prepare_p_s(
        self,
        p: Float[npt.ArrayLike, "..."] | None = None,
        s: Float[npt.ArrayLike, "..."] | None = None,
    ) -> tuple[Float[jax.Array, "..."], Float[jax.Array, "..."]]:
        if p is None:
            p = self.p
        else:
            self.reload(p)
        if s is None:
            s = self.s
        return jnp.asarray(p), jnp.asarray(s)

    @functools.cached_property
    def _fun_jit(
        self,
    ) -> Callable[
        [Float[jax.Array, " DoF"], Float[jax.Array, "..."], Float[jax.Array, "..."]],
        Float[jax.Array, ""],
    ]:
        return jax.jit(self._fun)

    def _jac(
        self,
        u: Float[jax.Array, " DoF"],
        p: Float[jax.Array, "..."],
        s: Float[jax.Array, "..."],
    ) -> Float[jax.Array, " DoF"]:
        return jax.grad(self._fun)(u, p, s)

    @functools.cached_property
    def _jac_jit(
        self,
    ) -> Callable[
        [Float[jax.Array, " DoF"], Float[jax.Array, "..."], Float[jax.Array, "..."]],
        Float[jax.Array, " DoF"],
    ]:
        return jax.jit(self._jac)

    def _hessp(
        self,
        u: Float[jax.Array, " DoF"],
        v: Float[jax.Array, " DoF"],
        p: Float[jax.Array, "..."],
        s: Float[jax.Array, "..."],
    ) -> Float[jax.Array, " DoF"]:
        fun = lambda u: self._fun(u, p, s)  # noqa: E731
        return gr.hvp(fun, u, v)

    @functools.cached_property
    def _hessp_jit(self) -> Callable[[], Float[jax.Array, " DoF"]]:
        return jax.jit(self._hessp)

    @abc.abstractmethod
    def _reload(self, p: jax.Array) -> Float[jax.Array, "..."]: ...
    @abc.abstractmethod
    def _fun(
        self,
        u: Float[jax.Array, " DoF"],
        p: Float[jax.Array, "..."],
        s: Float[jax.Array, "..."],
    ) -> Float[jax.Array, ""]: ...
