# deskrecorder — 终端/桌面(非浏览器)遗留系统批量录入：屏幕/OCR 定位(离线夹具)、映射填报、提交幂等、人工介入。

难度：**地狱**　|　子方向：数据采集 / 爬虫与 RPA　|　运行栈：Python 3.14 + 标准库 `sqlite3` + `httpx` + `pytest`（离线，无需联网）

## 基础版代码（起点，能跑）
读 `fixtures/input.json` → `loader` → `normalizer` → 其余已实现变换 → `keyer` → 幂等落 `sqlite`。
```
make run     # 跑通 happy-path，打印 {fed, rows}
make test    # happy-path + 幂等 + 缺口桩断言
```

## 单一职责约定
每个模块 = 一个文件 = 一个聚焦函数；`pipeline.py` 只做顺序编排、不含业务判断。
业务模块：`screen_locate, mapping, ocr_read, submit, batch, interrupt, audit` ＋ 通用 `loader / normalizer / keyer / store / pipeline / cli`。

## 故意留空（功能开发面）
- `screen_locate.py` → `process()` 抛 `NotImplementedError`（对记录做单一职责变换：screen_locate；功能开发目标，未接入 happy-path）
- `batch.py` → `process()` 抛 `NotImplementedError`（对记录做单一职责变换：batch；功能开发目标，未接入 happy-path）

## 朴素实现短板（功能优化面）
- `submit.py` → 朴素实现 + docstring 标注短板（对记录做单一职责变换：submit；功能优化目标）
- `audit.py` → 朴素实现 + docstring 标注短板（对记录做单一职责变换：audit；功能优化目标）

> 缺口模块刻意未接入 happy-path，以保证基线可运行；它们正是出题要补的 0→1 / 1→n 功能。
