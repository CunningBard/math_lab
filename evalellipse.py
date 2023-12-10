import math

USED_TYPE = lambda s: float(eval(s))

print("Points(Space separated):")
[F1x, F1y] = [USED_TYPE(val) for val in input("F1 Point: ").strip().split(" ")]
[F2x, F2y] = [USED_TYPE(val) for val in input("F2 Point: ").strip().split(" ")]


while True:
	point = input("Given Point: ").strip()
	if point.lower() in ["s", "stop", "exit", "e"]:
		break

	[Ax, Ay] = [USED_TYPE(val) for val in point.split(" ")]
	dst_f1 = math.sqrt((Ax - F1x) ** 2 + (Ay - F1y) ** 2)
	dst_f2 = math.sqrt((Ax - F2x) ** 2 + (Ay - F2y) ** 2)

	print(f"\t - Distance to F1: {dst_f1}")
	print(f"\t - Distance to F2: {dst_f2}")
	print(f"\t - Sum of Distances: {dst_f1 + dst_f2}")

