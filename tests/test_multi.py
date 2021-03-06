import unittest

import numpy as np
import numpy.linalg as la
import numpy.random as rnd
import numpy.testing as np_testing

from pymanopt.tools.multi import *


class TestMulti(unittest.TestCase):
    def setUp(self):
        self.m = m = 40
        self.n = n = 50
        self.p = p = 40
        self.k = k = 10

    def test_multiprod_singlemat(self):
        # Two random matrices A (m x n) and B (n x p)
        A = rnd.randn(self.m, self.n)
        B = rnd.randn(self.n, self.p)

        # Compare the products.
        np_testing.assert_allclose(A.dot(B), multiprod(A, B))

    def test_multiprod(self):
        # Two random arrays of matrices A (k x m x n) and B (k x n x p)
        A = rnd.randn(self.k, self.m, self.n)
        B = rnd.randn(self.k, self.n, self.p)

        C = np.zeros((self.k, self.m, self.p))
        for i in range(self.k):
            C[i] = A[i].dot(B[i])

        np_testing.assert_allclose(C, multiprod(A, B))

    def test_multitransp_singlemat(self):
        A = rnd.randn(self.m, self.n)
        np_testing.assert_array_equal(A.T, multitransp(A))

    def test_multitransp(self):
        A = rnd.randn(self.k, self.m, self.n)

        C = np.zeros((self.k, self.n, self.m))
        for i in range(self.k):
            C[i] = A[i].T

        np_testing.assert_array_equal(C, multitransp(A))

    def test_multisym(self):
        A = rnd.randn(self.k, self.m, self.m)

        C = np.zeros((self.k, self.m, self.m))
        for i in range(self.k):
            C[i] = .5 * (A[i] + A[i].T)

        np.testing.assert_allclose(C, multisym(A))
