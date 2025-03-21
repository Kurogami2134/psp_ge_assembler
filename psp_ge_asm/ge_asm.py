import struct
from typing import Any


class NotAlignedException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


def ge_asm(op_code, args: list[Any]):
    match op_code:
        case 'NOP':
            return b'\x00\x00\x00\x00'
        case 'VADDR':  # vaddr
            if args[0] & 0xFF000000 > 0:
                raise OverflowError('Vertex address outside of range')
            return struct.pack("I", args[0] & 0xFFFFFF | 0x01000000)
        case 'IADDR':  # vaddr
            if args[0] & 0xFF000000 > 0:
                raise OverflowError('Index address outside of range')
            return struct.pack("I", args[0] & 0xFFFFFF | 0x02000000)
        case 'PRIM':  # V_COUNT, PRIM
            return struct.pack("1H2B", *args, 4)
        case 'BEZIER':  # A x B
            return struct.pack("2BxB", *args, 5)
        case 'SPLINE':  # A x B type (C x D)
            return struct.pack("4B", args[0], args[1], (args[2] & 3) << 2 | args[3] & 3, 6)
        case 'JUMP':  # jump_address
            if args[0] & 0xFF000000 > 0:
                raise OverflowError('Jump address outside of range')
            if args[0] % 4 > 0:
                raise NotAlignedException('Jump address not word aligned')
            return struct.pack("I", args[0] & 0xFFFFFF | 0x08000000)
        case 'CALL':  # call address
            if args[0] & 0xFF000000 > 0:
                raise OverflowError('Call address outside of range')
            if args[0] % 4 > 0:
                raise NotAlignedException('Call address not word aligned')
            return struct.pack("I", args[0] & 0xFFFFFF | 0x0A000000)
        case 'RET':  # data*
            if len(args) < 1:
                args.append(0)
            if args[0] & 0xFF000000 > 0:
                raise OverflowError('Data size outside of range')
            return struct.pack("I", args[0] & 0xFFFFFF | 0x0B000000)
        case 'END':  # data*
            if len(args) < 1:
                args.append(0)
            if args[0] & 0xFF000000 > 0:
                raise OverflowError('Data size outside of range')
            return struct.pack("I", args[0] & 0xFFFFFF | 0x0C000000)
        case 'FINISH':  # data*
            if len(args) < 1:
                args.append(0)
            if args[0] & 0xFF000000 > 0:
                raise OverflowError('Data size outside of range')
            return struct.pack("I", args[0] & 0xFFFFFF | 0x0F000000)
        case 'BASE':  # base, extra*
            if len(args) < 2:
                args.append(0)
            if args[0] > 0xFF:
                raise OverflowError('Base outside of range')
            return struct.pack("H2B", args[1], args[0], 0x10)
        case 'VTYPE':  # bypass_transform, texture, color, normals, position, weight, weight_count, index
            while len(args) < 8:
                args.append(0)
            command = (args[0] & 1) << 23 | (args[5] & 3) << 9  | (max(0, args[6] - 1) & 7) << 14 | args[1] & 3 | \
                (args[2] & 7) << 2 | (args[3] & 3) << 5 | (args[4] & 3) << 7 | (args[7] & 3) << 11
            return struct.pack("I", command | 0x12000000)
        case 'OFFSET':  # offset >> 0x8
            if args[0] & 0xFF000000 > 0:
                raise OverflowError('Data size outside of range')
            return struct.pack("I", args[0] & 0xFFFFFF | 0x13000000)
        case 'ORIGIN':
            return b'\x00\x00\x00\x14'
        case 'REGION1':  # a, b
            return struct.pack("I", args[0] | args[1] << 10 | 0x15000000)
        case 'TME':  # enable_texture_map
            return struct.pack("I", args[0] | 0x1E000000)
        case 'ABE':  # alpha blending enable
            return struct.pack("I", args[0] | 0x21000000)
        case 'ATE':  # alpha test enable
            return struct.pack("I", args[0] | 0x22000000)
        case 'WORLDN': # func, world matrix number
            return struct.pack('B2xB', args[0], 0x3A)
        case 'WORLDD': # func, world matrix data
            return struct.pack("f", args[0])[1:] + b'\x3B'
        case 'VIEWN': # func, view matrix number
            return struct.pack('B2xB', args[0], 0x3C)
        case 'VIEWD': # func, view matrix data
            return struct.pack("f", args[0])[1:] + b'\x3D'
        case 'PROJN': # func, projection matrix number
            return struct.pack('B2xB', args[0], 0x3E)
        case 'PROJD': # func, projection matrix data
            return struct.pack("f", args[0])[1:] + b'\x3F'
        case "MEC":  # material emission color
            return struct.pack("I", args[0] | 0x54)
        case "MAC":  # material ambient color
            return struct.pack("I", args[0] | 0x55)
        case "MDC":  # material diffuse color
            return struct.pack("I", args[0] | 0x56)
        case "MSC":  # material specular color
            return struct.pack("I", args[0] | 0x57)
        case "MAA":  # material alpha
            return struct.pack("I", args[0] | 0x58)
        case "MK":  # material specular
            return struct.pack("f", args[0])[1:] + b'\x5B'
        case 'TBP0':  # texture0 pointer lower
            if args[0] & 0xFF000000 > 0:
                raise OverflowError('Pointer size outside of range')
            return struct.pack("I", args[0] & 0xFFFFFF | 0xA0000000)
        case 'TBW0':  # texture0 width, address high
            return struct.pack("H2B", args[0], args[1], 0xA8)
        case 'TSIZE0':  # texture0 widht, height (must be powers of two, indicated as exponent)
            return struct.pack("2BxB", *args, 0xB8)
        case 'TMODE':  # swizzle, separate_clut, levels
            return struct.pack("I", args[0] | args[1] << 8 | args[2] << 16 | 0xC2000000)
        case 'TPF':  # pixel format
            return struct.pack("B2xB", args[0], 0xC3)
        case 'TFILTER':  # min_filter, mag_filter
            return struct.pack("2BxB", *args, 0xC6)
        case 'TFUNC':  # func, rgba
            return struct.pack('2BxB', args[0], args[1], 0xC9)
        case 'TFLUSH':
            return b'\x00\x00\x00\xCB'
        case 'ATEST':  # and, value, op
            return struct.pack("4B", args[2], args[1], args[0], 0xDB)
        case _:
            raise NotImplementedError(f'The "{op_code}" op code is not yet implemented')
