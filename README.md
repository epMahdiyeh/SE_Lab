# Software Engineering Laboratory

This repository houses a collection of practical laboratory projects designed for a software engineering course. These projects are tailored to provide hands-on experience and practical application of software engineering principles, methodologies, and best practices.


## شرح آزمایش
در این آزمایش قصد پیاده‌سازی یک پروژه ماشین حساب ساده به زبان پایتون را داریم که عملیات جمع، تفریق، ضرب، تقسیم، توان و محاسبه سینوس یک زاویه را انجام می‌دهد.
برنچ‌هایی که در این ریپازیتوری طراحی شده اند بصورت زیر هستند:
develop: طراحی اولیه ساختار پروژه
feature: اضافه کردن توابع موردنیاز برای انجام عملیات
production: آپدیت و نهایی‌سازی قابلیت‌های پروژه
main: ادغام کدهای برنچ‌ها و ورژن پایانی کد 
همانطور که در صورت آزمایش خواسته شده، نهایتا منابع پروژه به برنچ main اضافه می‌شوند و از آنجا که این برنچ بصورت protected واقع شده، نیاز قطعی به انجام pull request برای دسترسی و ایجاد تغییر در این برنچ وجود دارد.
پس از اینکه در هر برنچ مربوطه، عملیات موردنیاز را پیاده‌سازی کردیم، به بررسی conflictهای محتمل پرداختیم. conflict زمانی رخ می‌دهد که بخشی از کد در دو برنچ مجزا توسط دو collaborator تغییر کند و بدون اینکه هر یک از آنها پروژه را در سیستم خود آپدیت کند و pull کرده باشد، درخواست merge کردن روی یک برنچ را داشته باشد. برای حل این مشکل باید این دو تغییر را مقایسه کرده و سپس یکی از آنها را به عنوان تغییر اصلی در برنچ انتخاب کرد و pull request ارسال کرد. تصاویر مربوط به این conflictها در فولدر pictures اضافه شده اند.
درنهایت نیز فایل readme با استفاده از pull request آپدیت شد.


## پاسخ سوالات

سوال 1.

پوشه‌ی .git در یک ریپازیتوری، حاوی اطلاعات مربوط به تاریخچه‌ی تغییرات، برنچ‌ها، و تنظیماتی‌ست که برای مدیریت نسخه مورد استفاده قرار می‌گیرد و پوشه‌ای پنهان است.
اطلاعات موجود در این پوشه:
سابقه کامیت‌ها: شامل اطلاعاتی مانند تاریخ، شخص کامیت‌کننده و پیام‌های کامیت مربوط به هر تغییر
اطلاعات برنچ‌ها: اطلاعات برنچ‌ها و ارتباط آن‌ها با هر کامیت
تنظیماتی که برای ریپازیتوری مشخص شده‌اند، مانند نام و ایمیل کامیت کننده و تنظیمات دیگر
فایل‌هایی که در این پوشه یافت می‌شوند عبارتند از: config، index، HEAD، ...
پوشه‌ی .git توسط دستور git init ایجاد می‌شود. این دستور یک ریپازیتوری جدید ایجاد کرده و پوشه‌ی .git را در دایرکتوری کنونی ایجاد می‌کند.

سوال 2.
 
 
مفهوم atomic در atomic commit و atomic pull-request به معنای اتمی یا ناپدیدپذیر بودن تغییرات است. وقتی یک کامیت یا pullrequest اتمی است، به این معنی است که تمام تغییرات مربوطه در یک عملیات ثابت اعمال شده و این عملیات به طور کامل و با موفقیت انجام می‌شود یا در صورت بروز خطا، هیچ تغییری در یپازیتوری اعمال نمی‌شود.
 
در مورد  atomic commit، وقتی تغییراتی را در فایل‌ها ایجاد می‌شود و بخواهیم آنها را کامیت کنیم، اگر کامیت از نوع اتمی باشد تمام تغییرات مربوط به کامیت در یک عملیات یکسان اعمال می‌شوند. درواقع اگر کامیت با موفقیت انجام شود، تمام تغییرات مربوط به کامیت در ریپو ثبت شده و در صورت بروز خطا، هیچ تغییری در آن انجام نمی‌شود.
 
در مورد atomic pullrequest، وقتی یک pullrequest در گیت ایجاد می‌شود و برای ادغام تغییراتی از یک شاخه به شاخه اصلی درخواست داده میشود، ادغام این تغییرات صرفاً در صورتی صورت می‌گیرد که تمام تغییرات مربوطه در pullrequest با موفقیت اعمال شوند. یعنی تغییرات در pullrequest به طور کامل و همزمان اعمال می‌شوند و در صورت بروز خطا، هیچ تغییری در شاخه اصلی انجام نمی‌شود. این ویژگی اتمیک pullrequest را از لحاظ امنیتی و تضمین صحت تغییرات مهم می‌کند، زیرا تغییرات در شاخه اصلی اعمال نمی‌شوند مگر اینکه همه تغییرات در pullrequest با موفقیت اعمال شده باشند.
  
 
  
سوال 3. 

 : Fetch دستور git fetch اطلاعات جدید از یک ریموت را دریافت می‌کند بدون آنکه آن را با شاخه قعلی ادغام کند. با اجرای این دستور، اطلاعات آخرین کامیت ها، شاخه‌ها و تگ‌ها از ریموت دریافت می‌شوند اما هیچ تغییری در شاخه‌های محلی ایجاد نمی‌شود.
 
 : Pullبا اجرای git pull، ابتدا اطلاعات جدید از ریموت باgit fetch  دریافت شده و سپس تغییرات را با استفاده از git merge در شاخه فعلی ادغام میکنیم. این دستور معمولاً برای به‌روزرسانی شاخه محلی و همچنین ادغام تغییرات از ریموت استفاده می‌شود.
 
 : Mergeدستور git merge برای ادغام تغییرات از یک شاخه (مانند شاخه فعلی یا شاخه دیگری) به شاخه فعلی استفاده می‌شود. یعنی تغییرات اعمال شده در شاخه مورد نظر با شاخه فعلی ادغام می‌شوند و یک کامیت جدید ایجاد می‌شود. این کایمت شامل تغییرات ادغام شده است و معمولاً برای ادغام شاخه‌های موازی کاربرد دارد.
 
 : Rebaseدستور git rebase برای اعمال تغییرات از یک شاخه به شاخه دیگر درخواست می‌شود، اما با استفاده از تغییر تاریخچه کامیت ها. به عبارتی کامیت های شاخه فعلی بر اساس کامیت های شاخه مورد نظر جابجا می‌شوند و تغییرات اعمال شده در شاخه فعلی بر روی نسخه جدیدی از کانیت ها اعمال می‌شوند.
 
 : Cherry-pickدستور git cherry-pick برای اعمال یک کامیت خاص از یک شاخه به شاخه فعلی استفاده می‌شود. با استفاده از این دستور، می‌توان کامیت مورد نظر را ازشاخه‌ای دیگر انتخاب کرد و در شاخه فعلی اعمال کرد. یک کامیت جدید با تغییرات کامیت انتخاب شده ایجاد می‌شود و به نوعی این کاربرد برای اعمال تغییرات خاص از یک شاخه به شاخه دیگر بدون ادغام کامل شاخه‌ها استفاده می‌شود.
 

سوال 4.
 
دستور reset برای بازگرداندن تغییرات در ریپازیتوری به وضعیت قبلی استفاده می‌شود. با اجرای دستور git reset و نشان دادن شناسه کامیت  مد نظر، می‌توان به حالت‌های مختلفی بازگشت.
دستورrevert  برای ایجاد یک کامیت جدید که تغییرات یک یا چند کامیت پیشین را بازگرداند، استفاده می‌شود. با اجرای این دستور و همچنین نشان دادن شناسه کامیت، یک کامیت جدید ایجاد می‌شود که تغییرات آن کامیت موردنظر را بر‌عکس می‌کند و تاریخچه ریپازیتوری تغییر نمی‌کند.
دستور restore در گیت برای بازگرداندن تغییرات یک یا چند فایل خاص در ریپو استفاده می‌شود. درواقع تغییرات اعمال شده در فایل‌ها به وضعیت قبلی برمیگردند. این دستور فقط بر روی فایل‌ها تأثیر می‌گذارد و تاریخچه کامیت ها را تغییر نمی‌دهد.
 
 
سوال 5.
 
 مرحله‌ی stage به معنای آماده‌سازی تغییرات برای کامیت است. وقتی تغییراتی در فایل‌های مختلفی انجام میشوند، ابتدا باید این تغییرات را به مرحله stage اضافه کرد تا بتوان آنها را در یک کامیت جدید ذخیره کرد. برای اضافه کردن تغییرات به stage، می‌توان از دستور git add استفاده کرد.
 
دستورstash برای ذخیره تغییرات موقت و پنهان کردن آنها استفاده می‌شود. وقتی تغییراتی در ریپو ایجاد میشوند ولی نمی‌خواهیم آنها را کامیت کنیم می‌توانیم از دستور git stash استفاده کنیم.
 با اجرای git stash، تغییرات unstaged (غیر آماده کامیت) و staged (آماده کامیت) ذخیره شده و ریپو به حالت بدون تغییرات برمیگردد. این دستور زمانی مفید است که مثلا نیاز داریم به شاخه دیگری منتقل شویم ولی تغییرات را تمام نکنیم. یا ممکن است تغییراتمان با کار دیگران تداخل داشته باشد. پس از اجرای این دستور، می‌توان به شاخه دیگری منتقل شد و بعداً با دستورgit stash apply تغییرات ذخیره شده را بازیابی کرد.
 
 
  
سوال 6.
 
مفهوم snapshot به معنای یک نسخه‌ کامل از مخزن در یک لحظه زمانی خاص است. این نسخه شامل تمام فایل‌ها و شرایط آنها در آن لحظه است. مثلا وقتی که تغییراتی در فایل‌های مختلف اعمال میشوند و آنها را با استفاده از دستور git add  به stage اضافه میکنیم، تغییراتی که در هر فایل انجام شده است، به صورت snapshot در مخزن ذخیره می‌شوند. هر کامیت جدیدی که انجام می‌شود، یک snapshot از وضعیت فعلی فایل‌ها را در مخزن ثبت می‌کند.
 
با استفاده از کامیت، میتوان به هر snapshot در تاریخچه ریپازیتوری برگشت و تغییرات را مشاهده یا بازیابی کرد. هر کامیت شامل یک شناسه یکتا، نویسنده، تاریخ و زمان ایجاد، و پیامی توضیح دهنده است. این شناسه به عنوان یک اشاره‌گر به snapshot مربوطه عمل می‌کند. ارتباطی که بین commit و snapshot وجود دارد، این امکان را می‌دهد که تغییراتی که در هر کامیت انجام شده را مشاهده و تاریخچه تغییرات را پیگیری کنیم.


