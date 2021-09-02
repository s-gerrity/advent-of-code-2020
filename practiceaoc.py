# day 5 practice



def find_rows(row_locator):
    max_rows = 127
    min_rows = 0
    
    i = 0
    while i <= len(row_locator):
        for indicator in row_locator:
            if indicator == 'F':

            if indicator == 'B':    
                divide_rows_upper_half = (max_rows - (max_rows / 2)) # 127 - (127 / 2) = 63
                print(divide_rows_upper_half, "divide_rows_upper_half")
                max_rows = 



def run_test(testValue, expectedResult, description):
  print(description)
  if (testValue == expectedResult):
    print('    ✅ Test passed')
  else:
    print('    ❌ Test failed!')


run_test(find_rows('FBFBBFF', 44, "Check first sample of finding a row")
