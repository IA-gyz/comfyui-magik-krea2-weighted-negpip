from typing_extensions import override
from comfy_api.latest import ComfyExtension, io

from .magik_krea2_weighted_negpip import MagikKREA2WeightedNegPIP


class MagikKREA2WeightedNegPIPExtension(ComfyExtension):
    @override
    async def get_node_list(self) -> list[type[io.ComfyNode]]:
        return [MagikKREA2WeightedNegPIP]


async def comfy_entrypoint() -> MagikKREA2WeightedNegPIPExtension:
    return MagikKREA2WeightedNegPIPExtension()
