# -*- coding: utf-8 -*-
"""
Часть I. Табличные интегралы для письмам (От базовых до диффуровских)
Разделы 1-4
"""

PART_INFO = {
    "i": 0,
    "name": "Часть I. Табличные интегралы для письмам (От базовых до диффуровских)",
    "color": "#0284c7"
}

SECTIONS = [
    {
        "n": 1,
        "p": 0,
        "t": "Раздел 1. Базовые табличные интегралы (Школьный и 1-й курс мастхэв)",
        "ts": "Базовые табличные интегралы"
    },
    {
        "n": 2,
        "p": 0,
        "t": "Раздел 2. Главные диффуровские интегралы: Арктангенс, высокий и длинный логарифм",
        "ts": "Диффуровские логарифмы и арктангенсы"
    },
    {
        "n": 3,
        "p": 0,
        "t": "Раздел 3. Тригонометрические интегралы для ДУ",
        "ts": "Тригонометрические интегралы"
    },
    {
        "n": 4,
        "p": 0,
        "t": "Раздел 4. Интегрирование по частям и расщепление дробей",
        "ts": "По частям и расщепление"
    }
]

CARDS = [
    # Раздел 1: Базовые интегралы
    {
        "s": 1,
        "p": 0,
        "q": r"Базовые степенные и экспоненциальные интегралы: $\int x^n dx$, $\int \frac{dx}{x}$, $\int e^{kx} dx$, $\int a^x dx$.",
        "a": r"""<p>📐 <b>Формулы:</b>
$$\int x^n dx = \frac{x^{n+1}}{n+1} + C \quad (n \ne -1)$$
$$\int \frac{dx}{x} = \ln|x| + C$$
$$\int e^{kx} dx = \frac{1}{k} e^{kx} + C$$
$$\int a^x dx = \frac{a^x}{\ln a} + C$$</p>
<p>⚠️ <b>Ловушка на письмакe:</b> Забыть модуль под логарифмом ($\ln|x|$, а не $\ln x$) или потерять коэффициент $\frac{1}{k}$ при интегрировании $e^{kx}$.</p>""",
        "f": False
    },
    {
        "s": 1,
        "p": 0,
        "q": r"Базовые тригонометрические интегралы: $\int \sin(kx)dx$, $\int \cos(kx)dx$, $\int \frac{dx}{\cos^2 x}$, $\int \frac{dx}{\sin^2 x}$.",
        "a": r"""<p>📐 <b>Формулы:</b>
$$\int \sin(kx)dx = -\frac{1}{k}\cos(kx) + C$$
$$\int \cos(kx)dx = \frac{1}{k}\sin(kx) + C$$
$$\int \frac{dx}{\cos^2 x} = \operatorname{tg} x + C$$
$$\int \frac{dx}{\sin^2 x} = -\operatorname{ctg} x + C$$</p>
<p>⚠️ <b>Ловушка на письмаке:</b> Знаки! Интеграл от синуса даёт <b>МИНУС</b> косинус ($-\cos$), а производная от косинуса даёт минус синус.</p>""",
        "f": False
    },
    {
        "s": 1,
        "p": 0,
        "q": r"Базовые интегралы от тангенса и котангенса: $\int \operatorname{tg} x\,dx$ и $\int \operatorname{ctg} x\,dx$.",
        "a": r"""<p>💡 <b>Откуда берётся:</b> Внесение под знак дифференциала: $\operatorname{tg} x = \frac{\sin x}{\cos x} = -\frac{d(\cos x)}{\cos x}$.</p>
<p>📐 <b>Формулы:</b>
$$\int \operatorname{tg} x\,dx = -\ln|\cos x| + C$$
$$\int \operatorname{ctg} x\,dx = \ln|\sin x| + C$$</p>""",
        "f": False
    },

    # Раздел 2: Диффуровские интегралы
    {
        "s": 2,
        "p": 0,
        "q": r"Чему равен интеграл $\int \frac{dx}{x^2 + a^2}$ и как интегрировать $\int \frac{dx}{x^2 + bx + c}$ при отрицательном дискриминанте?",
        "a": r"""<p>💡 <b>Откуда берётся:</b> Производная $(\operatorname{arctg} u)' = \frac{1}{1+u^2}$.</p>
<p>📐 <b>Формула:</b>
$$\int \frac{dx}{x^2 + a^2} = \frac{1}{a} \operatorname{arctg}\left(\frac{x}{a}\right) + C$$</p>
<p>⚙️ <b>Прямой алгоритм:</b>
1. Выделяем полный квадрат: $x^2 + bx + c = (x + b/2)^2 + (c - b^2/4) = (x + x_0)^2 + a^2$.
<br>2. Получаем: $\frac{1}{a}\operatorname{arctg}\left(\frac{x + x_0}{a}\right) + C$.</p>
<p>🎯 <b>Пример:</b> $\int \frac{dx}{x^2 + 2x + 5} = \int \frac{d(x+1)}{(x+1)^2 + 4} = \frac{1}{2}\operatorname{arctg}\left(\frac{x+1}{2}\right) + C$.</p>""",
        "f": False
    },
    {
        "s": 2,
        "p": 0,
        "q": r"Чему равен «высокий логарифм» $\int \frac{dx}{x^2 - a^2}$ и $\int \frac{dx}{a^2 - x^2}$?",
        "a": r"""<p>💡 <b>Откуда берётся:</b> Разложение дроби на простейшие: $\frac{1}{x^2-a^2} = \frac{1}{2a}\left(\frac{1}{x-a} - \frac{1}{x+a}\right)$.</p>
<p>📐 <b>Формулы:</b>
$$\int \frac{dx}{x^2 - a^2} = \frac{1}{2a} \ln \left| \frac{x - a}{x + a} \right| + C$$
$$\int \frac{dx}{a^2 - x^2} = \frac{1}{2a} \ln \left| \frac{a + x}{a - x} \right| + C$$</p>
<p>⚙️ <b>Мнемоника:</b> В числителе стоит тот множитель, с которого начинается разность квадратов: для $(x-a)(x+a)$ в числителе $(x-a)$; для $(a-x)(a+x)$ в числителе $(a+x)$.</p>
<p>🎯 <b>Пример:</b> $\int \frac{dx}{x^2 - 4} = \frac{1}{4}\ln\left|\frac{x-2}{x+2}\right| + C$.</p>""",
        "f": False
    },
    {
        "s": 2,
        "p": 0,
        "q": r"Чему равен «длинный логарифм» $\int \frac{dx}{\sqrt{x^2 \pm a^2}}$ и арксинус $\int \frac{dx}{\sqrt{a^2 - x^2}}$?",
        "a": r"""<p>📐 <b>Формулы:</b>
$$\int \frac{dx}{\sqrt{x^2 \pm a^2}} = \ln \left| x + \sqrt{x^2 \pm a^2} \right| + C \quad (\text{длинный логарифм})$$
$$\int \frac{dx}{\sqrt{a^2 - x^2}} = \arcsin\left(\frac{x}{a}\right) + C$$</p>
<p>⚠️ <b>Ловушка на письмаке:</b> Не путать минус перед $x^2$ (это $\arcsin$) и плюс/минус под корнем при $x^2$ (это длинный логарифм!). В длинном логарифме коэффициента $\frac{1}{a}$ перед логарифмом <b>НЕТ</b>!</p>
<p>🎯 <b>Пример:</b> $\int \frac{dx}{\sqrt{x^2 + 7}} = \ln(x + \sqrt{x^2+7}) + C$.</p>""",
        "f": False
    },

    # Раздел 3: Тригонометрические интегралы
    {
        "s": 3,
        "p": 0,
        "q": r"Чему равны интегралы $\int \frac{dx}{\sin x}$ и $\int \frac{dx}{\cos x}$?",
        "a": r"""<p>📐 <b>Формулы:</b>
$$\int \frac{dx}{\sin x} = \ln \left| \operatorname{tg} \frac{x}{2} \right| + C = \ln \left| \frac{1 - \cos x}{\sin x} \right| + C$$
$$\int \frac{dx}{\cos x} = \ln \left| \operatorname{tg} \left( \frac{x}{2} + \frac{\pi}{4} \right) \right| + C = \ln |\sec x + \operatorname{tg} x| + C$$</p>
<p>🎯 <b>Применение в ДУ:</b> Постоянно возникают при разделении переменных в уравнениях вида $y' = \frac{\sin x}{y}$ или $y' = y \cos x$.</p>""",
        "f": False
    },
    {
        "s": 3,
        "p": 0,
        "q": r"Как понижать степень для $\int \sin^2(kx) dx$ и $\int \cos^2(kx) dx$?",
        "a": r"""<p>💡 <b>Школьные формулы понижения степени:</b>
$$\sin^2(kx) = \frac{1 - \cos(2kx)}{2}, \qquad \cos^2(kx) = \frac{1 + \cos(2kx)}{2}$$</p>
<p>📐 <b>Интегралы:</b>
$$\int \sin^2(kx)dx = \frac{x}{2} - \frac{\sin(2kx)}{4k} + C$$
$$\int \cos^2(kx)dx = \frac{x}{2} + \frac{\sin(2kx)}{4k} + C$$</p>""",
        "f": False
    },

    # Раздел 4: По частям и расщепление
    {
        "s": 4,
        "p": 0,
        "q": r"Чему равны базовые интегралы по частям: $\int \ln x\,dx$, $\int \operatorname{arctg} x\,dx$, $\int \arcsin x\,dx$?",
        "a": r"""<p>💡 <b>Правило:</b> $u = f(x), dv = dx \implies \int u\,dv = u v - \int v\,du$.</p>
<p>📐 <b>Формулы:</b>
$$\int \ln x\,dx = x\ln x - x + C = x(\ln x - 1) + C$$
$$\int \operatorname{arctg} x\,dx = x\operatorname{arctg} x - \frac{1}{2}\ln(1 + x^2) + C$$
$$\int \arcsin x\,dx = x\arcsin x + \sqrt{1 - x^2} + C$$</p>""",
        "f": False
    },
    {
        "s": 4,
        "p": 0,
        "q": r"Как быстро в лоб брать $\int x e^{kx} dx$ и $\int x \cos(kx) dx$ по частям?",
        "a": r"""<p>📐 <b>Готовые формулы:</b>
$$\int x e^{kx} dx = \frac{x e^{kx}}{k} - \frac{e^{kx}}{k^2} + C = e^{kx}\left(\frac{x}{k} - \frac{1}{k^2}\right) + C$$
$$\int x \cos(kx) dx = \frac{x \sin(kx)}{k} + \frac{\cos(kx)}{k^2} + C$$
$$\int x \sin(kx) dx = -\frac{x \cos(kx)}{k} + \frac{\sin(kx)}{k^2} + C$$</p>
<p>🎯 <b>Применение:</b> Это самые частые интегралы при вариации постоянных в линейных ОДУ и системах с квазимногочленами!</p>""",
        "f": False
    },
    {
        "s": 4,
        "p": 0,
        "q": r"Как прямолинейно расщепить интеграл $\int \frac{px + q}{Ax^2 + Bx + C} dx$ на логарифм и арктангенс/высокий логарифм?",
        "a": r"""<p>💡 <b>Прямой алгоритм:</b>
1. Производная знаменателя: $(Ax^2 + Bx + C)' = 2Ax + B$.
<br>2. Выделяем эту производную в числителе:
$$px + q = \frac{p}{2A}(2Ax + B) + \left(q - \frac{pB}{2A}\right)$$
3. Интеграл разбивается на 2 табличных:
$$\int \frac{px+q}{Ax^2+Bx+C}dx = \frac{p}{2A}\ln|Ax^2+Bx+C| + \left(q - \frac{pB}{2A}\right)\int \frac{dx}{Ax^2+Bx+C}$$
Второй интеграл берется выделением полного квадрата ($\operatorname{arctg}$ или высокий логарифм).</p>""",
        "f": False
    }
]
