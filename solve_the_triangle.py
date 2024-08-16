"""                                     Văn Hiển - izcode                               """
import math

# Hàm nhập giá trị, nếu không nhập gì sẽ trả về None
def inp_or_none(enter):
    value = input(enter)
    return float(value) if value else None

def solve_triangle(a=None, b=None, c=None, A=None, B=None, C=None):
    try:
        if a and b and c:
            if a >= b + c or b >= a + c or c >= a + b:
                return "Lỗi: Các cạnh không hợp lệ cho một tam giác."
            A = round(math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c))), 2)
            B = round(math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c))), 2)
            C = 180 - A - B
        # Trường hợp ab^
        elif a and b and A:
            if a <= b * math.sin(math.radians(A)) or b <= a * math.sin(math.radians(A)):
                return "Lỗi: Giá trị góc A hoặc cạnh không hợp lệ."
            B = round(math.degrees(math.asin(b * math.sin(math.radians(A)) / a)), 2)
            C = 180 - A - B
            c = round(a * math.sin(math.radians(C)) / math.sin(math.radians(A)), 2)
        elif a and b and B:
            if b <= a * math.sin(math.radians(B)) or a <= b * math.sin(math.radians(B)):
                return "Lỗi: Giá trị góc B hoặc cạnh không hợp lệ."
            A = round(math.degrees(math.asin(a * math.sin(math.radians(B)) / b)), 2)
            C = 180 - A - B
            c = round(a * math.sin(math.radians(C)) / math.sin(math.radians(A)), 2)
        elif a and b and C:
            if a + b <= c or b + c <= a or a + c <= b:
                return "Lỗi: Các cạnh không hợp lệ cho một tam giác."
            c = round(math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(C))), 2)
            A = round(math.degrees(math.asin(a * math.sin(math.radians(C)) / c)), 2)
            B = 180 - A - C
        # Trường hợp ac^
        elif a and c and A:
            if a <= c * math.sin(math.radians(A)) or c <= a * math.sin(math.radians(A)):
                return "Lỗi: Giá trị góc A hoặc cạnh không hợp lệ."
            C = round(math.degrees(math.asin(c * math.sin(math.radians(A)) / a)), 2)
            B = 180 - A - C
            b = round(c * math.sin(math.radians(B)) / math.sin(math.radians(C)), 2)
        elif a and c and B:
            if b >= a + c or c >= a + b:
                return "Lỗi: Các cạnh không hợp lệ cho một tam giác."
            b = round(math.sqrt(a**2 + c**2 - 2 * a * c * math.cos(math.radians(B))), 2)
            A = round(math.degrees(math.asin(a * math.sin(math.radians(B)) / b)), 2)
            C = 180 - A - B
        elif a and c and C:
            if c >= a + b or a >= b + c:
                return "Lỗi: Các cạnh không hợp lệ cho một tam giác."
            A = round(math.degrees(math.asin(a * math.sin(math.radians(C)) / c)), 2)
            B = 180 - A - C
            b = round(a * math.sin(math.radians(B)) / math.sin(math.radians(A)), 2)
        # Trường hợp bc^
        elif b and c and A:
            if b >= a + c or c >= a + b:
                return "Lỗi: Các cạnh không hợp lệ cho một tam giác."
            a = round(math.sqrt(b**2 + c**2 - 2 * b * c * math.cos(math.radians(A))), 2)
            B = round(math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c))), 2)
            C = 180 - A - B
        elif b and c and B:
            if c >= a + b or a >= b + c:
                return "Lỗi: Các cạnh không hợp lệ cho một tam giác."
            C = round(math.degrees(math.asin(math.sin(math.radians(B)) * c / b)), 2)
            A = 180 - B - C
            a = round(b * math.sin(math.radians(A)) / math.sin(math.radians(B)), 2)
        elif b and c and C:
            if c >= a + b or a >= b + c:
                return "Lỗi: Các cạnh không hợp lệ cho một tam giác."
            B = round(math.degrees(math.asin(math.sin(math.radians(C)) * b / c)), 2)
            A = 180 - C - B
            a = round(b * math.sin(math.radians(A)) / math.sin(math.radians(B)), 2)
        # Trường hợp a^^
        elif a and A and B:
            C = 180 - B - A
            b = round(a * math.sin(math.radians(B)) / math.sin(math.radians(A)), 2)
            c = round(math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(C))), 2)
        elif a and A and C:
            B = 180 - A - C
            b = round(a * math.sin(math.radians(B)) / math.sin(math.radians(A)), 2)
            c = round(math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(C))), 2)
        elif a and B and C:
            A = 180 - B - C
            b = round(a * math.sin(math.radians(B)) / math.sin(math.radians(A)), 2)
            c = round(math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(C))), 2)
        # Trường hợp b^^
        elif b and A and B:
            C = 180 - A - B
            a = round(b * math.sin(math.radians(A)) / math.sin(math.radians(B)), 2)
            c = round(math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(C))), 2)
        elif b and A and C:
            B = 180 - A - C
            a = round(b * math.sin(math.radians(A)) / math.sin(math.radians(B)), 2)
            c = round(math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(C))), 2)
        elif b and B and C:
            A = 180 - B - C
            a = round(b * math.sin(math.radians(A)) / math.sin(math.radians(B)), 2)
            c = round(math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(C))), 2)
        # Trường hợp c^^
        elif c and A and B:
            C = 180 - A - B
            b = round(c * math.sin(math.radians(B)) / math.sin(math.radians(C)), 2)
            a = round(b * math.sin(math.radians(A)) / math.sin(math.radians(B)), 2)
        elif c and A and C:
            B = 180 - A - C
            b = round(c * math.sin(math.radians(B)) / math.sin(math.radians(C)), 2)
            a = round(b * math.sin(math.radians(A)) / math.sin(math.radians(B)), 2)
        elif c and B and C:
            A = 180 - B - C
            b = round(c * math.sin(math.radians(B)) / math.sin(math.radians(C)), 2)
            a = round(b * math.sin(math.radians(A)) / math.sin(math.radians(B)), 2)
        else:
            return "NaN. Lỗi: Không thể xử lý!"
        
        # Hàm xử lý góc
        def degrees(A, B, C):
            dga = str(int(A)) 
            dpga = str(int((A-int(A)) * 60))
            A = dga + "°" + dpga

            dgb = str(int(B)) 
            dpgb = str(int((B - int(B)) * 60))
            B = dgb + "°" + dpgb

            dgc = str(int(C)) 
            dpgc = str(int((C - int(C)) * 60))
            C = dgc + "°" + dpgc
            
            kq = f"""                     Trả Kết Quả
           Góc A: {A} Góc B: {B} Góc C: {C}
           Cạnh a: {round(a, 2)} Cạnh b: {round(b, 2)} Cạnh c: {round(c, 2)}"""
            return kq

        return degrees(A, B, C)
    
    except ValueError as ve:
        return f"""     Lỗi hệ thống 01: {str(ve)}"""
    except Exception as e:
        return f"""     Lỗi hệ thống 02: {str(e)}"""

# Nhập các giá trị cạnh và góc, cho phép giá trị là None
a = inp_or_none("Nhập cạnh a: ")
b = inp_or_none("Nhập cạnh b: ")
c = inp_or_none("Nhập cạnh c: ")
A = inp_or_none("Nhập góc A: ")
B = inp_or_none("Nhập góc B: ")
C = inp_or_none("Nhập góc C: ")

# Giải tam giác
result = solve_triangle(a, b, c, A, B, C)

# In kết quả
if isinstance(result, str) and "Lỗi hệ thống" in result:
    print(result)
else:
    print(result)
    
# code cũ bên dưới!
    
'''import math

#Hàm nhập giá trị nếu không nhập gì sẽ trả về None
def inp_or_none(enter):
    value = input(enter)
    return float(value) if value else None

def slove_triangle(a=None, b=None, c=None, A=None, B=None, C=None):
    if a and b and c:
        A = round(math.degrees(math.acos( (b**2 + c**2 - a**2) / (2*b*c) )),2)
        B = round(math.degrees(math.acos( (a**2 + c**2 - b**2) / (2*a*c) )),2)
        C = 180-A-B
# truong hop ab^
    elif a and b and A:
        B = round(math.degrees(math.asin( b * math.sin(math.radians(A) ) / a )),2)
        C = 180-A-B 
        c = round(a * math.sin(math.radians(C)) / math.sin(math.radians(A)),2)

    elif a and b and B:
        A = round(math.degrees(math.asin( a * math.sin(math.radians(B)) / b)),2)
        C = 180-A-B 
        c = round(a * math.sin(math.radians(C)) / math.sin(math.radians(A)),2)

    elif a and b and C:
        c = round(math.sqrt(a**2 + b**2 - 2 *a*b*math.cos(math.radians(C))),2)
        A = round(math.degrees(math.asin( a * math.sin(math.radians(C)) / c)),2)
        B = 180-A-C
# truong hop ac^
    elif a and c and A:
        C = round(math.degrees(( c * math.sin(math.radians(A)) / a )),2)
        B = 180-A-C
        b = round(c * math.sin(math.radians(B)) / math.sin(math.radians(C)),2)
        
    elif a and c and B:
        b = round(math.sqrt(a**2 + c**2 - 2 *a*c*math.cos(math.radians(B))),2)
        A = round(math.degrees(math.asin( a * math.sin(math.radians(B)) / b)),2)
        C = 180-A-B

    elif a and c and C:
        A = round(math.degrees(math.asin(a * math.sin(math.radians(C)) / c)),2)
        B = 180-A-C
        b = round(a * (math.sin(math.radians(B))) / (math.sin(math.radians(A))),2)
#truong hop bc^
    elif b and c and A:
        a = round(math.sqrt(b**2 + c**2 - 2 *b*c*math.cos(math.radians(A))),2)
        B = round( math.degrees( math.acos((a**2 + c**2 - b**2) / (2*a*c))),2)
        C = 180-A-B
    
    elif b and c and B:
        C = round(math.degrees( math.asin( math.sin( math.radians(B))*c / b)),2)
        A = 180-A-B
        a = round(b * (math.sin(math.radians(A))) / (math.asin(math.radians(B))),2)

    elif b and c and C:
        B = round(math.degrees( math.asin( math.sin( math.radians(C))*b / c)),2)
        A = 180-C-B
        a = round(b * (math.asin(math.radians(A))) / (math.asin(math.radians(B))),2)

#truong hop a^^
    elif a and A and B:
        C = 180-B-A
        b = round(a * (math.sin(math.radians(B))) / (math.sin(math.radians(A))),2)
        c = round(math.sqrt(a**2 + b**2 - 2 *a*b*math.cos(math.radians(C))),2)
    
    elif a and A and C:
        B = 180-A-C
        b = round(a * (math.sin(math.radians(B))) / (math.sin(math.radians(A))),2)
        c = round(math.sqrt(a**2 + b**2 - 2 *a*b*math.cos(math.radians(C))),2)

    elif a and B and C:
        A = 180-B-C
        b = round(a * (math.sin(math.radians(B))) / (math.sin(math.radians(A))),2)
        c = round(math.sqrt(a**2 + b**2 - 2 *a*b*math.cos(math.radians(C))),2)

# Truong hop b^^
    elif b and A and B:
        C = 180-A-B
        a = round(b * (math.asin(math.radians(A))) / (math.asin(math.radians(B))),2)
        c = round(math.sqrt(a**2 + b**2 - 2 *a*b*math.cos(math.radians(C))),2)

    elif b and A and C:
        B = 180-A-C
        a = round(b * (math.asin(math.radians(A))) / (math.asin(math.radians(B))),2)
        c = round(math.sqrt(a**2 + b**2 - 2 *a*b*math.cos(math.radians(C))),2)
    
    elif b and B and C:
        A = 180-B-C
        a = round(b * (math.asin(math.radians(A))) / (math.asin(math.radians(B))),2)
        c = round(math.sqrt(a**2 + b**2 - 2 *a*b*math.cos(math.radians(C))),2)
        
# Truong hop c^^
    elif c and A and B:
        C = 180 - A - B
        b = round(c * math.sin(math.radians(B)) / math.sin(math.radians(C)),2)
        a = round(b * (math.asin(math.radians(A))) / (math.asin(math.radians(B))),2)
    
    elif c and A and C:
        B = 180-A-C
        b = round(c * math.sin(math.radians(B)) / math.sin(math.radians(C)),2)
        a = round(b * (math.asin(math.radians(A))) / (math.asin(math.radians(B))),2)

    elif c and B and C:
        A = 180-B-C
        b = round(c * math.sin(math.radians(B)) / math.sin(math.radians(C)),2)
        a = round(b * (math.asin(math.radians(A))) / (math.asin(math.radians(B))),2)
    
    else:
        return "NaN. Loi KHong The Su Li!!"
    

    # Ham su li goc
    def degrees(A, B, C):
        dga = str(int(A)) 
        dpga = str(int((A-int(A))*60))
        A = dga +"°"+ dpga

        dgb = str(int(B)) 
        dpgb = str(int((B-int(B))*60))
        B = dgb +"°"+ dpgb

        dgc = str(int(C)) 
        dpgc = str(int((C-int(C))*60))
        C = dgc +"°"+ dpgc
        
        kq = f"""                   Trả Kết Quả
           Góc A: {A} Góc B: {B} Góc C: {C}
           Cạnh a: {round(a, 2)} Cạnh b: {round(b, 2)} Cạnh c: {round(c, 2)}"""
        return kq
    # In kết quả
    return degrees(A,B,C)
    
# Nhập các giá trị cạnh và góc, cho phép giá trị là None
a = inp_or_none("Nhập cạnh a: ")
b = inp_or_none("Nhập cạnh b: ")
c = inp_or_none("Nhập cạnh c: ")
A = inp_or_none("Nhập góc A: ")
B = inp_or_none("Nhập góc B: ")
C = inp_or_none("Nhập góc C: ")


# Giải tam giác
result =slove_triangle(a, b, c, A, B, C)

# In kết quả
if isinstance(result, str) and "Lỗi hệ thống" in result:
    print(result)
else:
    print(result)'''
