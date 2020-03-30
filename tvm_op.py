import numpy as np
import tvm
import topi

from __future__ import print_function, absolute_import

def element_wise_addition(shape, func_name, dtype="float32", tgt="llvm", tgt_host="llvm"):
    A = tvm.te.placeholder(shape, dtype=dtype, name="A")
    B = tvm.te.placeholder(shape, dtype=dtype, name="B")
    C = tvm.te.compute(A.shape, lambda *i: A(*i) + B(*i))

    s = tvm.te.create_schedule(C.op)
    f = tvm.build(s, [A, B, C], tgt, target_host=tgt_host, name=func_name)
    return f

def element_wise_addition_by_const(shape, const_k, func_name, dtype="float32", tgt="llvm", tgt_host="llvm"):
    A = tvm.te.placeholder(shape, dtype=dtype, name="A")
    B = tvm.tir.const(const_k, A.dtype)
    C = tvm.te.compute(A.shape, lambda *i: A(*i) + B)

    s = tvm.te.create_schedule(C.op)
    f = tvm.build(s, [A, C], tgt, target_host=tgt_host, name=func_name)
    return f

def element_wise_mul(shape, func_name, dtype="float32", tgt="llvm", tgt_host="llvm"):
    A = tvm.te.placeholder(shape, dtype=dtype, name="A")
    B = tvm.te.placeholder(shape, dtype=dtype, name="B")
    C = tvm.te.compute(A.shape, lambda *i: A(*i) * B(*i))

    s = tvm.te.create_schedule(C.op)
    f = tvm.build(s, [A, B, C], tgt, target_host=tgt_host, name=func_name)
    return f