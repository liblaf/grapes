import httpx
from mkdocs_gen_files.editor import FilesEditor

ASSETS: dict[str, str] = {
    "favicon.png": "https://raw.githubusercontent.com/microsoft/fluentui-emoji/main/assets/Grapes/3D/grapes_3d.png",
    "logo.png": "https://raw.githubusercontent.com/microsoft/fluentui-emoji/main/assets/Grapes/3D/grapes_3d.png",
}


editor: FilesEditor = FilesEditor.current()
for path, url in ASSETS.items():
    with editor.open(path, mode="wb") as fp:
        resp: httpx.Response = httpx.get(url)
        fp.write(resp.content)
