# 컨버터 한번에 관리하기

# Custom Path Converter 선언
class YearConverter:
	regex = r'20\d{2}'	# 2000년대에 해당되는 숫자 처리

	def to_python(self, value):
		return int(value)
	
	def to_url(self, value):
		return str(value)

class MonthConverter:
	regex = r'\d{1, 2}'	# 한개 혹은 두개의 숫자 처리

class DayConverter:
	regex = r'[0123]\d'
