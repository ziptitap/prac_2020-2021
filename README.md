Задание 1 состоит в численном решении антагонистической матричной игры. В
рамках данного задания мы:
• напишем код, решающий матричную игру путем сведения ее к паре
двойственных задач линейного программирования,
• проиллюстрируем работу данного кода путем визуализации спектров
оптимальных стратегий,
• напишем автоматические тесты для нашего решения.
Цель задания 1 заключается в том, чтобы познакомиться с языком
программирования Python, библиотекой SciPy, интерактивной средой
разработки Jupyter и с системой тестирования Nose.
Формально, задача заключается в следующем:
1. (25 баллов) Необходимо написать функция nash_equilibrium(a), которая
принимает матрицу выигрыша и возвращает значение игры и оптимальные
стратегии первого и второго игроков. ВАЖНО: нельзя использовать
функции-решения интегрированные в библиотеки. Например, если вы
собираетесь решать симплекс методом, то вы должны реализовать его
пошагово лично, а не использовать существующие готовые функции,
реализующие данный метод в python.
2. (25 баллов) Проиллюстрировать работу вашего кода путем решения
нескольких игр и визуализации спектров оптимальных стратегий игроков в
Jupyter. В частности, нужно привести игры, в которых:
i. спектр оптимальной стратегии состоит из одной точки (т.е. существует
равновесие Нэша в чистых стратегиях),
ii. спектр оптимальной стратегии неполон (т.е. некоторые чистые
стратегии не используются),
iii. спектр оптимальной стратегии полон.
3. (25 баллов) Оформить ваше решение в виде пакета [fn:packaging].
4. (25 баллов) Написать unit-тесты для функции nash_equilibrium [fn:testing].