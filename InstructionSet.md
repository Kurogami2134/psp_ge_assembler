# PSP GPU (GE) Assembly Instruction Set

Instruction set for the assembler.

## Index

- [NOP](#NOP)
- [VADDR](#VADDR)
- [IADDR](#IADDR)
- [PRIM](#PRIM)
- [BEZIER](#BEZIER)
- [SPLINE](#SPLINE)
- [JUMP](#JUMP)
- [CALL](#CALL)
- [RET](#RET)
- [END](#END)
- [FINISH](#FINISH)
- [BASE](#BASE)
- [VTYPE](#VTYPE)
- [OFFSET](#OFFSET)
- [ORIGIN](#ORIGIN)
- [REGION1](#REGION1)
- [TME](#TME)
- [ABE](#abe)
- [ATE](#ate)
- [MEC](#mec)
- [MAC](#mac)
- [MDC](#mdc)
- [MSC](#msc)
- [MAA](#maa)
- [MK](#mk)
- [TBP0](#TBP0)
- [TBW0](#TBW0)
- [TSIZE0](#TSIZE0)
- [TPF](#TPF)
- [TFUNC](#TFUNC)
- [TFLUSH](#TFLUSH)
- [ATEST](#atest)

## Instructions

### NOP

<b>Format</b>: NOP

<b>Purpose:</b> No Operation

To perform no operation.

### VADDR

<b>Format:</b> VADDR address

<b>Purpose:</b> Vertex Address

To set the starting address for the vertices to be used in the next draw

### IADDR

<b>Format:</b> IADDR address

<b>Purpose:</b> Index Address

To set the starting address for the indices to be used in the next draw.

### PRIM

<b>Format:</b> PRIM vertex_count, primitive

<b>Purpose:</b> Draw Primitive

To draw a primitive shape.

<b>Primitives:</b>

| Primitive           | Code |
|---------------------|------|
| PRIM_POINTS         | 0    |
| PRIM_LINES          | 1    |
| PRIM_LINE_STRIP     | 2    |
| PRIM_TRIANGLES      | 3    |
| PRIM_TRIANGLE_STRIP | 4    |
| PRIM_TRIANGLE_FAN   | 5    |
| PRIM_RECTANGLES     | 6    |

### BEZIER

<b>Format:</b> BEZIER x, y

<b>Purpose:</b> Draw Bezier

To draw a bezier surface.

### SPLINE

<b>Format:</b> SPLINE x, y, type, a, b

<b>Purpose:</b> Draw spline

To draw a spline surface.

### JUMP

<b>Format:</b> JUMP address

<b>Purpose:</b> Jump

To branch.

### CALL

<b>Format:</b> CALL address

<b>Purpose:</b> Call

To branch and link.

### RET

<b>Format:</b> RET

<b>Purpose:</b> Return

To return after call.

### END

<b>Format:</b> END

<b>Purpose:</b> End

To end reading.

### FINISH

<b>Format:</b> FINISH

<b>Purpose:</b> Finish

To finish drawing.

### BASE

<b>Format:</b> BASE high

<b>Purpose:</b> Set base

To set the base for the address used by [JUMP](#JUMP), [BJUMP](#BJUMP), [CALL](#CALL), [VADDR](#VADDR), and [IADDR](#IADDR).

### VTYPE

<b>Format:</b> VTYPE bypass_transform, texture, color, normals, position, weight, weight_count, index

<b>Purpose:</b> Set vertex type

To set the vertex type to be used in next draw.

<b>Description:</b> Sets vertex type according to codes for each field.

#### Vertex type settings

##### Weight

| Setting           | Code |
|-------------------|------|
| VTYPE_WEIGHT_NONE | 0    |
| VTYPE_WEIGHT_U8   | 1    |
| VTYPE_WEIGHT_U16  | 2    |
| VTYPE_WEIGHT_F    | 3    |

##### Texture

| Setting            | Code |
|--------------------|------|
| VTYPE_TEXTURE_NONE | 0    |
| VTYPE_TEXTURE_U8   | 1    |
| VTYPE_TEXTURE_U16  | 2    |
| VTYPE_TEXTURE_F    | 3    |

#### Color

| Setting            | Code |
|--------------------|------|
| VTYPE_COLOR_NONE   | 0    |
| VTYPE_COLOR_RGB565 | 4    |
| VTYPE_COLOR_RGBA5  | 5    |
| VTYPE_COLOR_RGBA4  | 6    |
| VTYPE_COLOR_RGBA8  | 7    |

#### Normals

| Setting            | Code |
|--------------------|------|
| VTYPE_NORMALS_NONE | 0    |
| VTYPE_NORMALS_S8   | 1    |
| VTYPE_NORMALS_S16  | 2    |
| VTYPE_NORMALS_F    | 3    |

#### Position

| Setting             | Code |
|---------------------|------|
| VTYPE_POSITION_NONE | 0    |
| VTYPE_POSITION_S8   | 1    |
| VTYPE_POSITION_S16  | 2    |
| VTYPE_POSITION_F    | 3    |

#### Index

| Setting          | Code |
|------------------|------|
| VTYPE_INDEX_NONE | 0    |
| VTYPE_INDEX_U8   | 1    |
| VTYPE_INDEX_U16  | 2    |
| VTYPE_INDEX_U32  | 3    |

### OFFSET

<b>Format:</b> OFFSET offset

<b>Purpose:</b> Set offset

To set the offset address.

### ORIGIN

<b>Format:</b> ORIGIN

<b>Purpose:</b> Set origin

To set the offset address to program counter.

### REGION1

<b>Format:</b> REGION x, y

<b>Purpose:</b> Set drawing region

To set the drawing region.

### TME

<b>Format:</b> TME enable

<b>Purpose:</b> Texture map enable

To enable or disable texture map.

### ABE

<b>Format:</b> ABE enable

<b>Purpose:</b> Alpha blending enable

To enable or disable alpha blending.

### ATE

<b>Format:</b> ATE enable

<b>Purpose:</b> Alpha test enable

To enable or disable alpha test.

### MEC

<b>Format:</b> MEC rgb8

<b>Purpose:</b> Material emission color

To set material emission color.

### MAC

<b>Format:</b> MAC rgb8

<b>Purpose:</b> Material ambient color

To set material ambient color.

### MDC

<b>Format:</b> MDC rgb8

<b>Purpose:</b> Material diffuse color

To set material diffuse color.

### MSC

<b>Format:</b> MSC rgb8

<b>Purpose:</b> Material specular color

To set material specular color.

### MAA

<b>Format:</b> MAA rgb8

<b>Purpose:</b> Material alpha color

To set material alpha color.

### MK

<b>Format:</b> MK spec_coefficient

<b>Purpose:</b> Model Specular

To set the specular coefficient of the model.

### TBP0

<b>Format:</b> TBP0 lower pointer

<b>Purpose:</b> Texture 0 base pointer

To set the lower for the pointer to texture 0.

### TBW0

<b>Format:</b> TBW0 stride, upper pointer

<b>Purpose:</b> Texture 0 stride

To set the upper pointer and stride for texture 0.

### TSIZE0

<b>Format:</b> TSIZE0 width, height

<b>Purpose:</b> Texture 0 size

To set the size for texture 0.

<b>Description:</b> Texture 0 size = 1 << width x 1 << height

### TPF

<b>Format:</b> TPF format

<b>Purpose:</b> Texture Pixel Format

To set pixel format for loaded texture.

<b>Pixel formats:</b>

| Format     | Code |
|------------|------|
| TPF_5650   | 0x0  |
| TPF_5551   | 0x1  |
| TPF_4444   | 0x2  |
| TPF_8888   | 0x3  |
| TPF_CLUT4  | 0x4  |
| TPF_CLUT8  | 0x5  |
| TPF_CLUT16 | 0x6  |
| TPF_CLUT32 | 0x7  |
| TPF_DXT1   | 0x8  |
| TPF_DXT3   | 0x9  |
| TPF_DXT5   | 0xA  |

### TFUNC

<b>Format:</b> TFUNC func, rgba

<b>Purpose:</b> Texture Function

To set the texture funcion, and transparency.

<b>Texture Functions:</b>

| Function       | Code |
|----------------|------|
| TFUNC_MODULATE | 0    |
| TFUNC_DECAL    | 1    |
| TFUNC_BLEND    | 2    |
| TFUNC_REPLACE  | 3    |
| TFUNC_ADD      | 4    |
| TFUNC_ADD2     | 5    |
| TFUNC_ADD3     | 6    |
| TFUNC_ADD4     | 7    |

### TFLUSH

<b>Format:</b> TFLUSH

<b>Purpose:</b> Texture Flush

To flush loaded texture.

### ATEST

<b>Format:</b> ATEST and, value, op

<b>Purpose:</b> Alpha Test

To set the alpha test parameters.

<b>Description:</b> if (a & and) op (value & and)

<b>Operator Codes:</b>

| Code | Operator|
|------|---------|
| 0x00 | NEVER   |
| 0x01 | ALWAYS  |
| 0x02 | ==      |
| 0x03 | !=      |
| 0x04 | <       |
| 0x05 | <=      |
| 0x06 | >       |
| 0x07 | >=      |
