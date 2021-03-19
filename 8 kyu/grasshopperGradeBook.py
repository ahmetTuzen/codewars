def get_grade(s1, s2, s3):
    avg = (s1 + s2 + s3) / 3
    return 'F' if avg < 60 else 'D' if avg < 70 else 'C' if avg < 80 else 'B' if avg < 90 else 'A'
