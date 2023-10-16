from dotenv import load_dotenv
import openai
import os
import re
import tiktoken


load_dotenv()
openai.api_key = os.getenv('API_KEY')



 
def non_english_filter(text):
	persian_chars = "ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهیءآأؤإئاب"
	persian_numerals = "۰۱۲۳۴۵۶۷۸۹"
	persian_chars_and_numerals = persian_chars + persian_numerals
	text_list = list(text)
	filtered_text = ''
	for ch in text_list:
		if ch in persian_chars_and_numerals:
			pass
		else:
			filtered_text+=ch
	return filtered_text


def writing_email(info, th=500):
	prompt = f'''
		Given the following information please compose an email for sending to a professor with a proper subject line that introduces the applicant and discusses collaboration opportunities. Keep in mind the Professor's name is {info['نام استاد']}, the institute's name is {info['دانشگاه یا مؤسسه آموزشی']}, the degree that the applicant is inquiring about is {info['مقطع تحصیلی']} and the field of study is {info['رشته تحصیلی']}. The applicant's name is {info['نام متقاضی']} and he/she is interested in {info['علایق پژوهشی متقاضی']} as research interests. The related experiences are {info['تجربیات کاری و آکادمیک']} and the email is attached with {info['موارد ضمیمه شده']}. Convert Persian expressions into proper English ones. 
	'''
	model_name = "gpt-4"

	encoding = tiktoken.encoding_for_model(model_name)
	token_count = len(encoding.encode(prompt))
	if token_count>th:
		return -1
	response = openai.ChatCompletion.create(
				  model=model_name,
				  messages=[{"role": "system", "content": prompt},
							{"role": "user", "content": 'Keep the email short under 200 words and well orgnized. Just use English not any other language'}],
				  )
	result = response['choices'][0]['message']['content']
	result = non_english_filter(result)
	return result

def test(info, th=500):
	return str(info)

if __name__=='__main__':
	info = {
		'مقطع تحصیلی':'دکترا',
		'نام استاد':'Barney May',
		'دانشگاه یا مؤسسه آموزشی':'دانشکده علوم کامپیوتر دانشگاه آکسفورد',
		'رشته تحصیلی':'مهندسی کامپیوتر',
		'نام متقاضی':'Mina Rahmati',
		'علایق پژوهشی متقاضی':'پردازش زبان طبیعی، یادگیری ماشین توضیح پذیر',
		'تجربیات کاری و آکادمیک':'یک مقاله کنفرانسی، دو مقاله ژورنالی و یکبار دستیاری استاد در درس یادگیری ماشین',
		'موارد ضمیمه شده':'رزومه، کارنامه کارشناسی، کارنامه کارشناسی ارشد'
	}
	print(writing_email(info))

