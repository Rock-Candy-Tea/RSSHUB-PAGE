
---
title: 'LCODER之JNI系列：C语言学习笔记'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=6497'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 06:04:35 GMT
thumbnail: 'https://picsum.photos/400/300?random=6497'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><ol>
<li></li>
</ol>
<p>.h .hpp 声明文件<br>
.c .cpp 实现文件<br>
#include 后面跟 "" 表示寻找自己写的资源 后面跟<>表示寻找系统的资源</p>
<ol start="2">
<li>打印：需要占位</li>
</ol>
<pre><code class="copyable">printf("i的值：%d\n",i); // int 类型 
printf("i的值：%lf\n",d); // double类型
printf("i的值：%f\n",f); // float 
printf("i的值：%d\n",l); // long
printf("i的值：%d\n",s); // short
printf("i的值：%c\n",c);// char
printf("i的地址：%p\n",c);// p : 地址占位符`
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>字符串类型</li>
</ol>
<pre><code class="copyable">char * str = "derry";
//打印：
printf("i的值：%s\n",str);// 字符串
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>常用的api</li>
</ol>
<pre><code class="copyable">sizeof() 获取字节数
sizeof(int); // int类型数据所占字节数
sizeof(double); // double类型数据所占字节数
sizeof(char); // char类型数据所占字节数
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5.指针  万物皆地址
指针 == 地址
地址：
int num = 10000;
printf("number变量的地址：%p\n",&num); // %p 地址占位符  & 取地址符
num指向10000的地址</p>
<p>指针：
& 取地址符 * 取值
int num_int = 100;
double num_double = 200;</p>
<p>printf("num_int的值：%d\n",num_int);
printf("num_double的值：%lf\n",num_double);
printf("num_int的值：%d\n",<em>(&num_int));
printf("num_int的值：%lf\n",</em>(&num_double));</p>
<p>指针变量： int *    |   double *    intP是指针变量，里面存放的是地址：是number_int的地址  * 是取值 取出该地址中的值
int * intP = &number_int;<br>
double * doubleP = &number_double;
printf("num_int的值：%d\n",*intP); // 打印的是number_int的值
printf("num_int的值：%lf\n",*doubleP);</p>
<p>函数不能写在main的下面
如果非要写在main的后面，要在main之前声明一下：
void change(int i);</p>
<p>int main()&#123;
int i = 100;
change(i);
printf("%d,%p\n",i,&i);
return 0;
&#125;</p>
<p>// 要和之前声明的一致
void change(int i)&#123;
i = 200;
printf("%d,%p\n",i,&i);
&#125;</p>
<p>打印结果：
200,0032FD8C
100,0032FD98</p>
<p>change函数中的行为参数，和main方法中传递进来的不是同一个参数，调用change方法时，change函数进栈。C/C++编译器会构建一个新的行参，和main函数的i没有半毛钱的关系，内存地址不同，无法修改。</p>
<p>解决：
要改掉main函数的i的值，需要找到main函数中i的地址：
void change(int * i);  // 参数是指针类型的变量
int main()&#123;
int i = 100;
change(&i); // 传入的是i的地址
printf("%d\n",i)
return 0;
&#125;
void change(int * i)&#123;
*i = 666; // 取出i地址对应的值修改为666
&#125;</p>
<p>输出结果：666</p>
<p>互换数值：</p>
<p>void changeAction(int * a, int * b)&#123;
int temp = *a; // 取出a地址对应的值 赋值给temp</p>
<pre><code class="copyable">*a = *b ;  // 取出b地址对应的值，赋值给a地址对应的值
*b = temp; // temp赋值给b地址对应的值
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<p>int main()&#123;
int a = 100;
int b = 200;</p>
<pre><code class="copyable">changeAction(&a , &b);
printf("互换后的效果：%d，%d\n",a,b)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<p>多级指针：
int num = 999;
int * num_p = # // 一级指针 存放num的地址
int ** num_p_p = &num_p; // 二级指针 存放num_p的地址</p>
<p>取值： **num_p_p  取出的值是：999</p>
<p>数组与指针：
数组的内存地址 = 第一元素的内存地址
int arr[] = &#123;1,2,3,4&#125;;
int i = 0;
for(i = 0; i < 4;++i)&#123;
printf("%d\n",arr[i]);
&#125;</p>
<p>printf("arr = %p\n",arr);
printf("&arr = %p\n",&arr);
printf("&arr[0] = %p\n",&arr[0]);
// 打印出来 三者相同</p>
<p>// 数组就是一个内存地址
int * arr_p = arr;
printf("%d\n",*arr_p); // 取出内存地址arr_p的值 ： 1</p>
<p>arr_p++; // 指针往数组的下一个移位</p>
<p>指针占用的内存大小： 4个字节 （32位系统）  4*2 = 8字节 （64位系统）</p>
<p>函数指针：万物皆指针，函数也有自己的指针 。 定义：返回值（*名称）（参数类型，参数类型） void(*method)(int,int)<br>
void add(int num1,int num2)&#123;
printf("num1 + num2 = %d\n",(num1 + num2));
&#125;</p>
<p>// void(*method)(int,int) 就是 函数指针
void operate(void(*method)(int,int),int num1,int num2))&#123;    method(num1,num2);
&#125;</p>
<p>int main()&#123;
operate(add,1,2); // 调用add函数</p>
<pre><code class="copyable">return 0;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<p>c语言速查文档：文档中 传入 &t &p 可以直接传入NULL尝试</p>
<p>C中的boolean类型  非0即true ， 0 == false</p>
<p>静态开辟：函数进栈时，定义数组或变量，就是属于静态吧
·开辟内存
静态开辟的内存空间大小，不能修改
栈区： 最大值 2M 大于2M会栈溢出
堆区： 最大值没有确定值，但基本上不用担心溢出</p>
<p>void staticAction()&#123;
int arr[5];  // 开辟 4*5 = 20 字节</p>
<pre><code class="copyable">for(int i = 0;i<5;++i)&#123;
    arr[i] = i ;
    printf("%d,%p\n",*(arr+i),arr+i);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;
// 虽然在死循环中开辟内存，但不会导致栈溢出异常，因为每次调用进栈，每次调用完毕就出栈
// 出栈后会释放所有的栈成员
int main()&#123;
while(9)&#123;
sleep(100);
staticAction(); // 在死循环中调用staticAction 每次调用都会进栈，静态开辟内存
&#125;
return 0;
&#125;</p>
<p>动态开辟：
使用malloc 等开辟堆区的内存  凡是在堆区开辟内存空间 都属于动态开辟</p>
<p>动态开辟的内存，不会被释放
// C开发的过程中，不能出现悬空指针和野指针，把二者置为NULL即可
//  int * p = NULL;
void dynamicAction()&#123;
int * p ; // 野指针，没有地址的指针
int * arr = malloc(1 * 1024 * 1024);
printf("dynamicAction函数，arr自己的内存地址：%p，堆区开辟的内存地址：%p\n",&arr,arr);</p>
<pre><code class="copyable">// 重复释放会导致崩溃，所以先判断一下
if(arr)&#123;
 free(arr);
// 释放之后，需要把arr指向NULL 否则会出现悬空指针 
// 也就是 arr指向一块被释放掉的内存 
arr = NULL;  // NULL ：0x0000
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<p>int main()&#123;
while(9)&#123;
sleep(100);
dynamicAction();
&#125;
&#125;</p>
<p>动态开辟的使用场景：
int * arr = malloc(sizeof(int) * 8); // 动态开辟8 * 4 个字节的大小
for(int i = 0;i < 8;i++)&#123;
arr[i] = i;
&#125;</p>
<p>动态开辟 realloc 在堆中追加开辟内存
int * arr = (int <em>)realloc(arr,sizeof(int)</em>(num + new_num));
realloc(void * 首次开辟的指针，size总大小);
新开辟的内存的指针大部分情况下和首次开辟的指针一样
传入参数解释：首次开辟的指针、size总大小  为了避免内存空间不够，
当内存不够时，首次开辟指针是为了copy前面的几个数值。</p>
<p>字符串的两种表现方式：
int main()&#123;
// '\0'是给printf的，printf遇到\0才会停止打印 否则会在derry后面输出系统值
char str[] = &#123;'D','e','r','r','y','\0'&#125;;
str[2] = 'z';
printf("第一种方式：&s\n",str);</p>
<pre><code class="copyable">// 运行这段代码时，会造成崩溃，因为str2是一个地址值，
// 指向的是全局区里面的数据，全局区里面的数据拒绝访问
char * str2 = "Derry";
str2[2] = 'z';
printf("第二种方式：%s\n",str);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<p>指针挪动获取字符串信息：
int getLen(char * string)&#123;
int count = 0;
while(*string)&#123; // *string != '\0' 我就一直循环
string++;// 指针挪动  string 是数组，数组string指向的是数组第一个数值所在的地址
count++;
&#125;
return count;
&#125;</p>
<p>// 这种方式无法获得真正的len
void getLen2(int intarr[])&#123;
int len = sizeof(intarr)/sizeof(int);
printf("getLen的长度是%d\n",len); // 这里打印1
&#125;</p>
<p>void getLen3(int * resultLen,int intarr[])&#123;
// 手动计算长度
int count = 0;
while(*intarr)&#123;
intarr++;
count++;
&#125;
*resultLen = count; //找到resultLen地址 ， 把count值放入resultLen中
&#125;</p>
<p>int main()&#123;
char string[] = &#123;'A','B','C','D','0','\0'&#125;
int r = getLen(string);
printf("长度是：%d\n",r);// 输出结果是5</p>
<pre><code class="copyable">int intarr[] = &#123;1,2,3,4,5,6,7&#125;;
int len = sizeof(intarr)/sizeof(int);
print("len长度是：%d\n",len);  // 打印7 

// c/c++ 编译器，数组作为参数传递，会把数组优化成指针（为了高效率）
getLen2(intarr);

int result;
getLen3(&result,intarr); // &result 取出result地址 给函数，函数再给地址赋值
printf("getLen的长度是:%d\n",result);

return 0;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<p>CLion快捷键： 两次shift  输入File Encoding 改变Encoding
字符串的转换
使用函数： atoi 转换成整型
int main()&#123;
char * num = "1"; // 输出1
num = "12.68xx";  // 输出12</p>
<pre><code class="copyable">int result = atoi(num);
if(result)&#123; // 非0即true 不是0进入if  0就是转换失败了
    printf("恭喜你转换成功：%d\n",result)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;
atof 转换成double类型</p>
<p>字符串的比较
使用函数strcmp  返回0表示相等，返回1不相等 区分大小写  strcmpi 不区分大小写</p>
<p>字符串的查找、包含、拼接
函数： strstr 在串中查找指定字符串的第一次出现 返回指针  看是否包含，也使用这个函数
char * pop = strstr(str1,str2);
if(pop)&#123; // 非NULL 进入 查找到了
printf("查找到了，pop的值是：%s\n",pop);
&#125;else&#123;
printf("没有查找到\n");
&#125;</p>
<p>字符串的拼接： 使用函数： strcat
char destination[25]; // 容器 大小25
char * blank = "--到--" , *CPP = "C++" , *Java = "Java";
strcpy(destination,CPP); // 先copy到数组里面去
strcat(destination,blank);// 然后 再拼接
strcat(destination,Java);// 然后再拼接
printf("拼接后的结果：%s\n",destination);</p>
<p>大小写转换
void lower(char * dest,char * name)&#123;
char * temp;// 避免破坏name指针
while(temp)&#123;
*dest = tolower(*name);
temp++;// 挪动指针的位置++
dest++; // 挪动指针的位置 ++ 挪动一个存储一个 挪动一个存储一个
&#125;
*dest = '\0';  // 指针最后一个赋值'\0' 避免printf打印系统值
&#125;</p>
<p>int main()&#123;
char * name = "Derry";</p>
<pre><code class="copyable">// 先定义结果
char dest[20];
lower(dest,name);
printf("小写转换后的结构是：%s\n",dest);
return 0;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<p>字符串截取
void subStr1(char * result,char * str,int start,int end)&#123;
char * temp = str;// 定义临时指针，不破坏str指针
int count = 0; // 记录当前的位置
while(*temp)&#123;
if(count > start && count < end)&#123;
*result = *temp;
result++; // 接收值也要挪动，挪动指针来接收 temp给我的值
&#125;
temp ++;
count ++;
&#125;
&#125;</p>
<p>// 二级指针，使用的时候传递地址进来 使用&取地址
void subStr2(char ** result,char * str,int start,int end)&#123;
char * temp = str; //定义临时指针，不破坏str</p>
<pre><code class="copyable">// char resultArr[end - start];// 栈内存，在方法结束时，会被释放
// 开辟堆内存 
char * resultArr = malloc(end - start);
int count = 0;
for(int i = start;i<end;++i)&#123;
    resultArr[count] = *(temp+i);
    count++;
&#125;
// 取出二级指针中存放的一级指针
*result = resultArr;
printf("%s\n",resultArr);

// 这种方式，方法调用完之后要回收堆空间
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<p>void subStr3(char * result,char * str,int start,int end)&#123;
for(int i = start; i < end ;++i)&#123;
*(result +i) = *(str+i);
&#125;
&#125;</p>
<p>void subStr4(char * result,char * str,int start,int end)&#123;
// 参数1 ： 最终copy到result容器里面
// 参数2：  直接指针挪动到r
// 参数3：  从r开始挪动，挪动多少
strncpy(result,str+start,end-start);
&#125;</p></div>  
</div>
            