from Framework import *

tool = Tool()
rotate = Rotate()
chunk = Chunk()
var = Variable()
exp = Expression()
src = Source()

view("프로그램이 시작되었습니다.")

rotate.reset(0)
tool.expand()

delay(1000)

chunk.define("default", [30, 40, 50, 60])
rotate.chunk(chunk.get("default"))

delay(1000)

var.define("input", int_read("수량을 입력하세요."))

exp.IF(var.get("input") < 0, src.function)