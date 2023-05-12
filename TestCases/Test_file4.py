import pytest



class Test_004:

   @pytest.mark.skip
   @pytest.mark.group1
   def test_mul_002(self):
        a = 5
        b = 7
        mul = a * b
        if mul == 35:
            print("test_mul_001 is Passed")
            assert True
        else:
            print("test_mul_001 is failed")
            assert False

