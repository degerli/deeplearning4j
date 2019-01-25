# automatically generated by the FlatBuffers compiler, do not modify

# namespace: graph

import flatbuffers

class UIHardwareState(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsUIHardwareState(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UIHardwareState()
        x.Init(buf, n + offset)
        return x

    # UIHardwareState
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UIHardwareState
    def GpuMemory(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # UIHardwareState
    def GpuMemoryAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # UIHardwareState
    def GpuMemoryLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UIHardwareState
    def HostMemory(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def UIHardwareStateStart(builder): builder.StartObject(2)
def UIHardwareStateAddGpuMemory(builder, gpuMemory): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(gpuMemory), 0)
def UIHardwareStateStartGpuMemoryVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def UIHardwareStateAddHostMemory(builder, hostMemory): builder.PrependInt64Slot(1, hostMemory, 0)
def UIHardwareStateEnd(builder): return builder.EndObject()