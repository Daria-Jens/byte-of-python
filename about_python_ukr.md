# Про мову програмування Python

Python — одна з тих рідкісних мов, які можуть бути водночас _простими_ і _потужними_. Ви будете приємно здивовані, побачивши, як легко зосередитися на вирішенні поставленого завдання, а не на синтаксисі та структурі мови, на якій ви програмуєте.

Офіційно мову Python представляють так:

> Python — це потужна мова програмування, яка проста у вивченні. Вона має ефективні високорівневі структури даних та простий, але ефективний підхід до об’єктно-орієнтованого програмування. Елегантний синтаксис і динамічна типізація мови Python разом із інтерпретованою природою роблять ії ідеальною мовою для створення сценаріїв і швидкої розробки додатків у багатьох сферах на більшості платформ.

Більш детально я розповім про більшість із цих особливостей у наступному розділі.

## Історія, що стоїть за назвою

Гвідо ван Россум, автор мови програмування Python, назвав свою розробку на честь телешоу на
BBC під назвою "Літаючий Цирк Монті Пайтона"(англ."Monty Python's Flying Circus"). 
А зовсім не тому,що він любить змій, які вбивають тварин для їжі шляхом звивання
їхніх довгих тіл навколо них і розчавлювання їх.

## Особливості Python

### Проста мова програмування

Python — проста та мінімалістична мова. Читання якісного коду на мові Python виглядає майже як читання англійською, хоча англійська дуже сувора! Така «псевдокодова» природа мови Python є однією з ії найбільших переваг. Це дозволяє зосередитися на вирішенні завдання, а не на самій мові.

### Легкість у вивченні

Як ви побачите,з мови Python дуже легко почати програмувати. Python має надзвичайно простий синтаксис, як уже згадувалося.

### Вільне і відкрите програмне забезпечення

Python є прикладом _ВВПЗ_ (Вільне та Відкрите Програмне Забезпечення), (англ."_FLOSS_" (Free/Libre and Open Source Software)).Простіше кажучи, ви можете вільно поширювати копії цього програмного забезпечення, читати його вихідний код, вносити в нього зміни та використовувати його частини в нових безкоштовних програмах. ВВПЗ базується на концепції спільноти, яка ділиться знаннями. Це одна з причин, чому мова Python така гарна - вона була створена і постійно вдосконалюється спільнотою, яка  прагнуть зробити мову ще кращою.

### Мова високого рівня

Коли ви пишете програми на мові Python, вам ніколи не доведеться турбуватися про деталі низького рівня, такі, як наприклад, керування пам’ятю, яку використовує ваша програма, тощо.

### Python — портативна мова програмування

Через свою відкриту природу, мова Python була портована на (тобто змінена, щоб змусити її працювати на) багатьох платформах. Усі ваші програми на мові Python можуть працювати на будь-якій із цих платформ, не вимагаючи жодних змін, якщо ви будете достатньо обережні, щоб уникнути будь-яких системно-залежних функцій.
Ви можете використовувати мову Python на GNU/Linux, Windows, FreeBSD, Macintosh, Solaris, OS/2, Amiga, AROS, AS/400, BeOS, OS/390, z/OS, Palm OS, QNX, VMS, Psion, Acorn RISC OS, VxWorks, PlayStation, Sharp Zaurus, Windows CE і PocketPC!

Ви навіть можете використовувати таку платформу, як [Kivy](http://kivy.org), щоб створювати ігри для свого комп’ютера _і_ для iPhone, iPad і Android.

### Інтерпретована мова

Це вимагає трохи пояснень.

Програма, написана компільованою мовою програмування, як наприклад, C або C\+ +, перетворюється з вихідного коду(тобто C або C++) на мову, зрозумілу компьютеру (бінарний код, тобто нулі та одиниці), використовуючи компілятор з різними опціями. Коли ви запускаєте програму, компонувальник/завантажувач (англ."linker/loader software") копіює програму з жорсткого диска в оперативну пам’ять і починає її виконання.

Мова Python, напроти, не потребує компіляції у бінарний код. Ви просто _запускаєте_ програму безпосередньо з вихідного коду(англ."source code"). Aвтоматично мова Python перетворює вихідний код у деяку проміжну форму, звану байт-кодами, а потім перекладає байт-коди на рідну мову вашого комп’ютера (бінарний код), і запускає. Все це, насправді, значно полегшує використання мови Python, оскільки вам не потрібно турбуватися про компіляцію програми, переконуватися, що відповідні бібліотеки пов’язані та завантажені тощо.Це також робить ваші програми на Python набагато більш портативними, оскільки ви можете просто скопіювати свою програму,написану мовою Python на інший комп’ютер, і вона просто запрацює!

### Об'єктно-орієнтоване програмування

Мова Python підтримує процедурно-орієнтоване програмування, а також об’єктно-орієнтоване програмування (ООП). У _процедурно-орієнтованих_ мовах програма побудована навколо процедур або функцій, які є не що інше, як багаторазові частини програм. У _об’єктно-орієнтованих_ мовах програма побудована навколо об’єктів, які поєднують дані та функціонал. Python має дуже простий, але потужний спосіб створення ООП, особливо в порівнянні з такими великими мовами, як C++ або Java.

### Розширювана мова

Якщо вам потрібно,щоб деякий критичний фрагмент коду працював дуже швидко, або ви хочете, щоб якийсь фрагмент алгоритму не був відкритим для інших, ви можете програмувати цю частину вашої програми на мові C або C\++, а потім викликати її з ваших програм на мові Python.

### Можливість вбудовування

Ви можете вбудовувати Python у свої програми C/C\++, щоб надати користувачам "_scripting_ capabilities" (можливості  написати маленький фрагмент коду на мові Python всередені вашої великої програми(наприклад, C/C\++,Java,тощо )).


### Обширні бібліотеки

Стандартна бібліотека мови Python дійсно величезна. Вона може допомогти з вирішенням самих різноманітних завдань, пов'язаних з використанням регулярних виразів, генеруваням документації, перевіркою блоків коду, розпаралелювання процесів, базами даних, веб-браузерами, CGI, FTP, електронною поштою, XML, XML-RPC, HTML, файлами WAV, криптографією, GUI (графічними інтерфейсами користувача), та іншими системно-залежними речами. Пам’ятайте, що все це завжди доступно, де б не було встановлено Python. Це називається філософією Python _Все в комплекті_ ("_Batteries Included_" ).

Крім стандартної бібліотеки, існують інші високоякісні бібліотеки, які ви можете знайти в [каталозі пакетів Python](http://pypi.python.org/pypi).

### Резюме

Мова Python справді захоплююча та потужна. Вона має правильне поєднання продуктивність і можливості, які роблять написання програм на мові Python одночасно цікавим і легким.

## Різниця між версією Python 3 та 2

Ви можете проігнорувати цей розділ, якщо вас не цікавить різниця між версіями «Python 2» і «Python 3». Але майте на увазі, яку версію ви використовуєте. Ця книга написана для версії Python 3.

Пам’ятайте, що як тільки ви правильно зрозумієте та навчитеся використовувати одну версію, ви зможете легко дізнатися про відмінності та використовувати іншу. Найважче – навчитися програмуванню та зрозуміти основи самої мови Python.Це наша мета в цій книзі, і коли ви досягнете цієї мети, ви зможете легко використовувати Python 2 або Python 3 залежно від вашої ситуації.

Докладніше про відмінності між Python 2 і Python 3 дивиться:

- [Майбутнє Python 2 (англ."The future of Python 2")](http://lwn.net/Articles/547191/)
- [Перенесення коду Python 2 на Python 3 (англ."Porting Python 2 Code to Python 3")](https://docs.python.org/3/howto/pyporting.html)
- [Написання коду, який працює на Python2 і 3(англ."Writing code that runs under both Python 2 and 3")](https://wiki.python.org/moin/PortingToPy3k/BilingualQuickRef)
- [Підтримка Python 3: докладний посібник(англ."Supporting Python 3: An in-depth guide")](http://python3porting.com)

## Що кажуть програмісти

Можливо, вам буде цікаво почитати, що такі великі хакери, як Ерік С. Реймонд (ESR), мають сказати про Python:

- _Ерік Стівен Реймонд_ є автором книги «Собор і базар», а також людиною, яка ввела термін _відкритого програмного забезпечення_. Він каже, що [Python став його улюбленою мовою програмування](http://www.python.org/about/success/esr/). Ця стаття стала справжнім натхненням моїх перших робіт з Python.
- _Брюс Екель_ є автором знаменитих книг «Мислення на Java» та «Мислення на C++». Він каже, що жодна мова не зробила його більш продуктивним, ніж мова Python. Він вважає, що Python, мабуть, єдина мова, яка спрямована на полегшення роботи програміста. Прочитайте [повне інтерв’ю](http://www.artima.com/intv/aboutme.html), щоб дізнатися більше.
- _Пітер Норвіг_ — відомий автор Lisp і директор із якості пошуку в Google (дякую Гвідо ван Россуму за те, що звернув увагу на це). Він каже, що [написання на Python — це все одно, що написання в псевдокоді](https://news.ycombinator.com/item?id=1803815). Він каже, що Python завжди був невід’ємною частиною Google. Ви можете перевірити це твердження, переглянувши сторінку [Вакансії в Google](http://www.google.com/jobs/index.html), на якій знання Python є обов’язковими для інженерів програмного забезпечення.
