import csv
# csv 파일을 읽고 처리하기 위한 라이브러리

import io
# 문자열 데이터를 파일처럼 다루기 위한 라이브러리

FIELDS = ['product', 'quantity', 'price']
# CSV 파일에 반드시 있어야 하는 열 이름과 순서 지정

def parse_sales(raw):
    # CSV 파일의 원본 데이터(raw)를 읽고 검사하는 함수
    # parse_sales(raw) 개발자 함수라 변경가능 

    if len(raw) > 100_000:
        # 파일 크기가 100,000바이트(약 100KB)를 초과하는지 확인
        # len은 파일 크기 확인

        raise ValueError('파일은 100kb 이하로 준비하세요')
    # 조건에 맞지 않으면 오류 발생

    try:
        text = raw.decode('utf-8-sig')
        # UTF-8 형식으로 데이터를 문자열로 변환
        # utf-8-sig는 엑셀에서 저장한 UTF-8 BOM도 처리 가능

        reader = csv.DictReader(io.StringIO(text), strict=True)
        # 문자열을 파일처럼 만들어 CSV 읽기
        # DictReader는 각 행을 딕셔너리 형태로 읽음
        # strict=True는 잘못된 CSV 형식을 검사

        if reader.fieldnames != FIELDS:
            # CSV의 첫 번째 행(열 이름)이 지정한 순서와 같은지 확인
            #필드명을 읽어줘라

            raise ValueError('필수 열 순서: product,quantity,price')
            #raise는 예외를 발생시키다
            # 열 이름이나 순서가 다르면 오류 발생

        rows = []
        # 검사에 통과한 데이터를 저장할 빈 리스트 생성

        for number, source in enumerate(reader, 2):
            # CSV 데이터를 한 줄씩 읽기
        # enumerate(reader, 2)는 실제 CSV의 2번째 줄부터 번호 부여

            print(source)
            # 현재 읽은 행의 데이터를 출력

            if len(rows) >= 1000:
                raise ValueError('데이터는 1000행 이하로 준비하세요')
             # 데이터가 1000행 이상이면 오류 발생

            if set(source) != set(FIELDS) or None in source.values():
                raise ValueError(f'{number}번째 레코드의 열을 확인하세요.')
            # 열 이름이 올바른지 확인
            # None in source.values()는 비어 있는 추가 열이 있는지 확인


            product = source['product'].strip()
             # 상품명에서 앞뒤 공백 제거

            if not product or len(product) > 40:
                raise ValueError('상품명은 1~40글자입니다')
            # 상품명이 비어 있거나 40글자를 초과하면 오류 발생

            numeric = []
              # 수량과 가격을 저장할 빈 리스트 생성

            for name in ['quantity', 'price']:
                # quantity와 price를 하나씩 검사

                value = source[name].strip()
                 # 해당 데이터의 앞뒤 공백 제거

                if not value.isascii() or not value.isdecimal():
                    raise ValueError(f'{name}에는 양의 정수를 입력하세요')
                # 숫자가 아닌 값이거나 영문 숫자 체계가 아니면 오류 발생
                # isascii() : 아스키 문자로 구성되어 있는지 확인
                # isdecimal() : 0~9의 십진수인지 확인

                value = int(value)
                # 문자열을 정수형 숫자로 변환

                if not 1 <= value <=1_000_000:
                    raise ValueError(f'{name}는 1~100000 범위 입니다.')
                elif value == int:
                    raise ValueError('숫자만 입력하세요')
                # 수량과 가격이 1~1,000,000 범위인지 확인

                numeric.append(value)
                 # 검사에 통과한 숫자를 리스트에 추가

            rows.append(dict(product=product, quantity=numeric[0], price = numeric[1]))
            # 검사에 통과한 데이터를 딕셔너리로 만들어 리스트에 추가

        return rows
     # 모든 데이터 검사가 끝나면 결과 반환

    except UnicodeDecodeError as exc:
        raise ValueError('UTF-8 CSV를 사용하세요') from exc
     # UTF-8 형식이 아닌 경우 오류 처리

    except csv.Error as exc:
        raise ValueError('CSV 형식을 확인하세요') from exc
    # CSV 파일 형식에 문제가 있는 경우 오류 처리

def summarize(rows):
    # 상품별 매출과 전체 매출을 계산하는 함수

    by_product = {}
    # 상품별 매출을 저장할 빈 딕셔너리 생성

    for row in rows:
        # 검사된 상품 데이터를 하나씩 반복

        name = row['product']
         # 현재 상품의 이름 가져오기

        by_product[name] = by_product.get(name, 0) + row['quantity'] * row['price']
        # 상품별 매출 계산
        # 기존 매출이 있으면 더하고, 없으면 0부터 시작
        # 수량 × 가격을 상품별 매출에 누적
        

        # 모든 상품의 매출과 판매 수량을 계산하여 딕셔너리로 반환
    return {'revenue':sum(by_product.values()), # 전체 매출액 계산
               'quantity':sum(row['quantity'] for row in rows),# 전체 판매 수량 계산
               'by_product':by_product}# 상품별 매출 내역 반환