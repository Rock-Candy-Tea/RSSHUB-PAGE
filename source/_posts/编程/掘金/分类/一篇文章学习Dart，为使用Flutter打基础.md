
---
title: '一篇文章学习Dart，为使用Flutter打基础'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c18f972b4464fc4b6b034f973f60e36~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 24 Mar 2021 22:44:38 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c18f972b4464fc4b6b034f973f60e36~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0"><a href="https://juejin.cn/post/6943478965856108558"></a>安装</h4>
<p><a href="https://dart.dev/get-dart" target="_blank" rel="nofollow noopener noreferrer">Dart官网</a><br>
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c18f972b4464fc4b6b034f973f60e36~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-1"><a href="https://juejin.cn/post/6943478965856108558"></a>安装brew</h5>
<p><a href="https://brew.sh/" target="_blank" rel="nofollow noopener noreferrer">Brew安装</a><br>
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/018d8a874abb4b948e98c2e01dccf4b8~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-2"><a href="https://juejin.cn/post/6943478965856108558"></a>执行代码</h5>
<pre><code class="hljs language-js copyable" lang="js">/bin/bash -c <span class="hljs-string">"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/214ca13e6a4843cd8f195a18e411ef9f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-3"><a href="https://juejin.cn/post/6943478965856108558"></a>使用BREW安装Dart的SDK</h5>
<pre><code class="hljs language-js copyable" lang="js">$ brew tap dart-lang/dart
$ brew install dart
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8fe11ae5d90849468a59a4e9135e0680~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><br>
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3447a2dbb79b4e39b684228bcb748eff~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>安装的过程如果有代理的，需要将代理关掉，不然会提示安装失败</li>
</ul>
<h5 data-id="heading-4"><a href="https://juejin.cn/post/6943478965856108558"></a>检测Dart是否安装成功：dart info</h5>
<p><img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/707868fc8fbb41baa291ac7d7b8663a9~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-5"><a href="https://juejin.cn/post/6943478965856108558"></a>使用vscode编写dart文件</h5>
<ul>
<li>需要安装两个插件：code runner 和 Dart</li>
</ul>
<p><img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e1172d4a8cc4b8991c159e033049e14~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><br>
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52498c4c68da44b680108c0438a05889~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>至此就可以使用您的电脑开发Dart了</p>
</blockquote>
<h4 data-id="heading-6"><a href="https://juejin.cn/post/6943478965856108558"></a>认识Dart</h4>
<blockquote>
<p>Dart这门语言比较奇葩一点，他拥有很多java的特性，但是写法却和js很像，学习这门语言的根本目的也是不得已而为之，毕竟学习flutter的话，dart不学习是不行的，这篇文章就是简单的写一下dart中我们需要注意的一些点，和js以及java的不同之处，如果您有java和js的基础的话，那么学习这门语言将会异常的简单。这篇文章写的比较简单，包括demo写的都是一些超级简单的，目的很明确，了解dart这门语言就可以，具体说我们使用其实要结合flutter进行使用，同时我个人认为的是这篇文章的人都是有js或者java或者两者都有基础的人阅读的，所以是没有什么压力的。本片章重点介绍和和js以及java中的一些出入，避免这些出入以后可以说Dart就已经会使用了！</p>
</blockquote>
<h4 data-id="heading-7"><a href="https://juejin.cn/post/6943478965856108558"></a>基本语法概述</h4>
<blockquote>
<p>基本的写法和js保持一致，写一个简单的demo，包含了基本的写法,强调几个点和js的区别</p>
</blockquote>
<ul>
<li>常量：和js语法一致，均是使用const，但是多了一个final进行声明，比如：const pi = 3.1415 Or final PI = 3.14</li>
<li>Dart是一种相对智能的语言，有自己的语法检测，比如定义了string类型，在后面重新赋值了int类型的情况会提示错误。</li>
<li>Dart是区分大小写的，var str 和var STR 是两个变量</li>
<li>Dart是严格使用分号的，结尾不加分号会报错</li>
<li>和js语法基本一致，可以使用var声明，Dart会根据赋值来判断类型，但是不支持Js的let声明，也同样适应java语法，使用数据类型进行声明，比如：String str = ‘hello’ int Num = 1234等</li>
<li>Dart获取值是通过“$&#123;变量&#125;”进行获取</li>
<li>Dart中万物皆是Object</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//自定义无参函数</span>
int <span class="hljs-function"><span class="hljs-title">num</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-number">123</span>;
&#125;
<span class="hljs-comment">//自定义必填参数函数</span>
<span class="hljs-built_in">String</span> <span class="hljs-function"><span class="hljs-title">UserInfos</span>(<span class="hljs-params"><span class="hljs-built_in">String</span> name, int age</span>)</span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">"姓名：$name 年龄：$age"</span>;
&#125;
<span class="hljs-comment">//自定义非必填参数函数  默认返回的是null 可选参数可以是多个，全部写在[]里面即可 当然也可以在参数里面直接默认赋值</span>
<span class="hljs-built_in">String</span> <span class="hljs-function"><span class="hljs-title">getUserInfos</span>(<span class="hljs-params"><span class="hljs-built_in">String</span> name, [<span class="hljs-built_in">String</span> sex]</span>)</span> &#123;
  <span class="hljs-keyword">if</span> (sex != <span class="hljs-literal">null</span>) <span class="hljs-keyword">return</span> <span class="hljs-string">"姓名：$name 性别：$sex"</span>;
  <span class="hljs-keyword">return</span> <span class="hljs-string">"姓名：$name 性别保密"</span>;
&#125;
<span class="hljs-comment">//自定义一个命名参数</span>
<span class="hljs-built_in">String</span> <span class="hljs-function"><span class="hljs-title">ObjUserInfos</span>(<span class="hljs-params"><span class="hljs-built_in">String</span> name, &#123;<span class="hljs-built_in">String</span> sex&#125;</span>)</span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">"姓名：$name 性别：$sex"</span>;
&#125;
<span class="hljs-comment">//入口函数</span>
<span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">main</span>(<span class="hljs-params"></span>)</span> &#123;
  print(num());
  print(UserInfos(<span class="hljs-string">"tom"</span>, <span class="hljs-number">25</span>));
  print(getUserInfos(<span class="hljs-string">"tom"</span>));
  print(ObjUserInfos(<span class="hljs-string">"tom"</span>, <span class="hljs-attr">sex</span>: <span class="hljs-string">'男'</span>));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8"><a href="https://juejin.cn/post/6943478965856108558"></a>main方法</h4>
<blockquote>
<p>这个是dart语言的最最最主要的一个方法，也是所有函数执行的入口函数，和java中的main方法以及c语言中的main函数拥有一样的位置，这里的重要性就不需要再提了吧！</p>
</blockquote>
<h4 data-id="heading-9"><a href="https://juejin.cn/post/6943478965856108558"></a>变量、常量</h4>
<blockquote>
<p>变量就是可变的量，比如定义了一个String name name就是一个变量，常量就是不可以改变的量，const pi = 3.14， pi就是一个常量</p>
</blockquote>
<h4 data-id="heading-10"><a href="https://juejin.cn/post/6943478965856108558"></a>函数</h4>
<blockquote>
<p>将一段实现某一个功能的一段代码进行封装起来的方法就是函数</p>
</blockquote>
<h5 data-id="heading-11"><a href="https://juejin.cn/post/6943478965856108558"></a>静态</h5>
<blockquote>
<p>静态属性和方法，使用static进行修饰的属性和方法就叫做静态属性和方法，直接通过类进行调用,静态方法不可以访问非静态的成员，但是非静态的方法可以访问静态的成员</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Info</span> </span>&#123;
<span class="hljs-built_in">String</span> name;
int age;
<span class="hljs-keyword">static</span> <span class="hljs-built_in">String</span> sex;
<span class="hljs-function"><span class="hljs-title">infoFun</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name; <span class="hljs-comment">//使用this访问的是非静态属性</span>
&#125;

<span class="hljs-comment">//静态方法不可以访问非静态的属性和方法</span>
<span class="hljs-keyword">static</span> <span class="hljs-built_in">String</span> <span class="hljs-function"><span class="hljs-title">staFun</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-keyword">return</span> sex; <span class="hljs-comment">//不需要this，直接使用属性，调用静态方法也是一样的，直接调用就可以</span>
&#125;
&#125;

<span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">main</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-keyword">var</span> i = <span class="hljs-keyword">new</span> Info();
i.name;
i.age;
Info.sex; <span class="hljs-comment">//静态的属性直接使用类进行访问</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-12"><a href="https://juejin.cn/post/6943478965856108558"></a>默认的get、set方法</h5>
<blockquote>
<p>和普通的方法的区别就是调用的时候需不需要加小括号</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Areafun</span> </span>&#123;
  int height;
  int width;
  <span class="hljs-comment">//构造函数第一种默认值的写法</span>
  <span class="hljs-comment">//Areafun(this.height, this.width) &#123;&#125;</span>
  <span class="hljs-comment">//构造函数第二种默认值有值的写法</span>
  Areafun()
      : <span class="hljs-built_in">this</span>.height = <span class="hljs-number">10</span>,
        <span class="hljs-built_in">this</span>.width = <span class="hljs-number">4</span> &#123;&#125;
  <span class="hljs-comment">//还有一种默认的get set方法</span>
  get areavalue &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.height * <span class="hljs-built_in">this</span>.width;
  &#125;

  <span class="hljs-comment">//默认的set方法</span>
  <span class="hljs-keyword">set</span> <span class="hljs-title">areaNewValue</span>(<span class="hljs-params">int value</span>) &#123;
    <span class="hljs-built_in">this</span>.height = value;
  &#125;

  <span class="hljs-function"><span class="hljs-title">comArea</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.height * <span class="hljs-built_in">this</span>.width;
  &#125;
&#125;

<span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">main</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">var</span> area = <span class="hljs-keyword">new</span> Areafun();
  print(area.comArea());
  print(area.areavalue); <span class="hljs-comment">//此时不需要加小括号</span>
  area.areaNewValue = <span class="hljs-number">45</span>;
  print(area.areavalue);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-13"><a href="https://juejin.cn/post/6943478965856108558"></a>闭包</h5>
<blockquote>
<p>了解闭包之前先要了解一下什么是局部变量和全局变量，这里就说一下他们各自的特点，具体什么是全局变量和局部变量，看文章的人没有不知道的应该，全局变量：常驻内存，污染全局，局部变量：不会常驻内存，会被垃圾回收，不会污染全局，让一个变量常驻内存，但是又不污染全局，这个就是闭包的意义所在，实现一个闭包也很简单，函数嵌套函数，内部函数调用外部函数的变量或者参数，并return 里面的函数就形成了闭包</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">main</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-function"><span class="hljs-title">printInfo</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-keyword">var</span> a = <span class="hljs-number">123</span>;
<span class="hljs-keyword">return</span> () &#123;
a++;
print(a);
&#125;;
&#125;

<span class="hljs-keyword">var</span> b = printInfo();
b();
b();
b();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-14"><a href="https://juejin.cn/post/6943478965856108558"></a>递归</h5>
<blockquote>
<p>下面的demo里面有匿名函数，递归函数，和自执行函数，所谓的递归就是轮循自己进行一些功能的实现，通过某一个条件进行终止自身的循环的一种写法</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//匿名函数</span>
<span class="hljs-keyword">var</span> num = (int n) &#123;
  <span class="hljs-keyword">return</span> n;
&#125;;
<span class="hljs-comment">//递归函数</span>
<span class="hljs-keyword">var</span> sum = <span class="hljs-number">1</span>;
<span class="hljs-function"><span class="hljs-title">fn</span>(<span class="hljs-params">int n</span>)</span> &#123;
  sum *= n;
  <span class="hljs-keyword">if</span> (n == <span class="hljs-number">1</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
  &#125;
  fn(n - <span class="hljs-number">1</span>);
&#125;

<span class="hljs-comment">//入口函数</span>
<span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">main</span>(<span class="hljs-params"></span>)</span> &#123;
  print(num(<span class="hljs-number">12</span>));
  <span class="hljs-comment">//自执行函数</span>
  (() &#123;
    print(<span class="hljs-string">'is Run'</span>);
  &#125;)();
  <span class="hljs-comment">//调用</span>
  fn(<span class="hljs-number">8</span>);
  print(sum);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15"><a href="https://juejin.cn/post/6943478965856108558"></a>操作符</h4>
<blockquote>
<p>? 条件运算符 as 类型转换 is 类型判断 …级联操作（连缀），下面的demo主要演示连缀的操作，别的基本和js是一致的。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Info</span> </span>&#123;
  <span class="hljs-built_in">String</span> name;
  int age;
  <span class="hljs-function"><span class="hljs-title">Info</span>(<span class="hljs-params"><span class="hljs-built_in">this</span>.name, <span class="hljs-built_in">this</span>.age</span>)</span> &#123;&#125;
  <span class="hljs-function"><span class="hljs-title">printInfo</span>(<span class="hljs-params"></span>)</span> &#123;
    print(<span class="hljs-string">"$&#123;this.name&#125;:$&#123;this.age&#125;"</span>);
  &#125;
&#125;
<span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">main</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-comment">//常规写法</span>
  <span class="hljs-keyword">var</span> p = <span class="hljs-keyword">new</span> Info(<span class="hljs-string">'张三'</span>, <span class="hljs-number">20</span>);
  p.name = <span class="hljs-string">'tom'</span>;
  p.age = <span class="hljs-number">26</span>;
  p.printInfo();
  <span class="hljs-comment">//连缀写法</span>
  p
    ..name = <span class="hljs-string">'jim'</span>
    ..age = <span class="hljs-number">30</span>
    ..printInfo();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16"><a href="https://juejin.cn/post/6943478965856108558"></a>类</h4>
<blockquote>
<p>Dart是一门面向对象编程的语言,它具有封装、继承、多态的特性，Dart是一门使用类和单继承的面向对象的语言，所有的对象都是类的实例，并且所有的类都是Object的子类，Dart中所有的东西都是对象，所有的对象都是继承自Object类，类：属性和方法组成：比如系统的List，Map都属于类</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-built_in">String</span> name = <span class="hljs-string">'tom'</span>;
  int age = <span class="hljs-number">23</span>;
  <span class="hljs-comment">//构造函数</span>
  <span class="hljs-comment">// Person() &#123;</span>
  <span class="hljs-comment">//   print("我是构造函数，我被实例化的时候就会执行");</span>
  <span class="hljs-comment">// &#125;</span>
  <span class="hljs-function"><span class="hljs-title">Person</span>(<span class="hljs-params"><span class="hljs-built_in">this</span>.name, <span class="hljs-built_in">this</span>.age</span>)</span> &#123;
    print(<span class="hljs-string">"我是构造函数，我被实例化的时候就会执行"</span>);
  &#125;
  <span class="hljs-comment">//命名构造函数可以第一多个</span>
  Person.now() &#123;
    print(<span class="hljs-string">"我是命名构造函数，我被实例化的时候就会执行"</span>);
  &#125;
  Person.setInfo(name, age) &#123;
    print(<span class="hljs-string">"我是命名构造函数，我被实例化的时候就会执行"</span>);
  &#125;
  <span class="hljs-function"><span class="hljs-title">setInfo</span>(<span class="hljs-params">int age</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.age = age;
  &#125;

  <span class="hljs-function"><span class="hljs-title">getInfo</span>(<span class="hljs-params"></span>)</span> &#123;
    print(<span class="hljs-string">'$&#123;this.name&#125; , $&#123;this.age&#125;'</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-17"><a href="https://juejin.cn/post/6943478965856108558"></a>封装、私有变量、公有变量以及构造函数</h5>
<blockquote>
<p>似有变量就是只能在自己的类中使用，在被引入的文件中是不可以被调用的，共有的变量就是，可以在自身类中被调用意外，还可以在被引入的时候调用，构造函数是在该类被初始化的时候就开始进行执行的函数，这里为什么将封装也写到这里了呢？因为私有变量在dart的封装性中可以得以体现！</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//这是一个具有私有变量的类，似有变量是在前面加上下划线</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span> </span>&#123;
  <span class="hljs-built_in">String</span> _name; <span class="hljs-comment">//此时的name是似有变量</span>
  int _age;
  <span class="hljs-built_in">String</span> sex; <span class="hljs-comment">//这个不加下划线的时候是一个共有的方法</span>
  <span class="hljs-function"><span class="hljs-title">Animal</span>(<span class="hljs-params"></span>)</span> &#123;
    print(<span class="hljs-string">"我是初始化的时候就会执行的构造函数"</span>);
  &#125;
  <span class="hljs-comment">// 此时的getInfo的函数是一个共有的函数，可以将私有的属性return出去为共有的属性</span>
  <span class="hljs-built_in">String</span> <span class="hljs-function"><span class="hljs-title">getInfo</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._name;
  &#125;

  <span class="hljs-comment">//这是一个私有的函数</span>
  <span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">_run</span>(<span class="hljs-params"></span>)</span> &#123;
    print(<span class="hljs-string">'我是一个私有的函数'</span>);
  &#125;

  <span class="hljs-comment">//这是一个共有的函数，执行的是一个私有的函数</span>
  <span class="hljs-function"><span class="hljs-title">execFun</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>._run();
  &#125;
&#125;
<span class="hljs-comment">//另一个文件可以通过import进行引入</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'lib/Animal.dart'</span>;
<span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">main</span>(<span class="hljs-params"></span>)</span> &#123;
  Animal a = <span class="hljs-keyword">new</span> Animal();
  a.sex;
  a.execFun();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-18"><a href="https://juejin.cn/post/6943478965856108558"></a>继承</h5>
<blockquote>
<p>通过extends进行实现,继承以后，子类拥有了父类的方法和属性，但是需要注意的是如果父类中拥有构造函数的话，子类继承的父类的时候需要将构造函数实现掉，当然子类也可以重写父类的方法，不过这里有一个常规的约定就是你可以直接实现父类方法一样的名字，但是一般我们都加上@override关键字</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
  <span class="hljs-built_in">String</span> name = <span class="hljs-string">'tom'</span>;
  int age;
  <span class="hljs-built_in">String</span> <span class="hljs-function"><span class="hljs-title">getInfo</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
  &#125;
&#125;

<span class="hljs-comment">//Child 继承了Person类，进而得到了Person的属性和方法，当然这是没有构造函数的情况</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Child</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Person</span> </span>&#123;&#125;

<span class="hljs-comment">//具有构造函数的类</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Man</span> </span>&#123;
  <span class="hljs-built_in">String</span> name;
  int age;
  <span class="hljs-built_in">String</span> sex;
  <span class="hljs-built_in">String</span> <span class="hljs-function"><span class="hljs-title">getInfo</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name;
  &#125;

  <span class="hljs-comment">//构造函数</span>
  <span class="hljs-function"><span class="hljs-title">Man</span>(<span class="hljs-params"><span class="hljs-built_in">this</span>.name, <span class="hljs-built_in">this</span>.age</span>)</span> &#123;&#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Boy</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Man</span> </span>&#123;
  Boy(<span class="hljs-built_in">String</span> name, int age, <span class="hljs-built_in">String</span> sex) : <span class="hljs-function"><span class="hljs-title">super</span>(<span class="hljs-params">name, age</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.sex = sex;
  &#125;
  <span class="hljs-built_in">String</span> <span class="hljs-function"><span class="hljs-title">exec</span>(<span class="hljs-params"></span>)</span> &#123;
    print(<span class="hljs-string">"$&#123;this.name&#125; --- $&#123;this.age&#125; --- $&#123;this.sex&#125;"</span>);
  &#125;
&#125;

<span class="hljs-comment">//复写父类的方法</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span> </span>&#123;
  <span class="hljs-built_in">String</span> name = <span class="hljs-string">'Dog'</span>;
  <span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">info</span>(<span class="hljs-params"></span>)</span> &#123;
    print(<span class="hljs-string">"$&#123;this.name&#125;"</span>);
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Animal</span> </span>&#123;
  <span class="hljs-built_in">String</span> name = <span class="hljs-string">'sheep'</span>;
  <span class="hljs-comment">//重写父类的方法  这里不加@override也是可以的，一般会加上</span>
  @override
  <span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">info</span>(<span class="hljs-params"></span>)</span> &#123;
    print(<span class="hljs-string">"$&#123;this.name&#125;"</span>);
  &#125;
&#125;

<span class="hljs-comment">//子类调用父类的方法</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Factory</span> </span>&#123;
  <span class="hljs-built_in">String</span> name = <span class="hljs-string">'FAC'</span>;
  <span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">run</span>(<span class="hljs-params"></span>)</span> &#123;
    print(<span class="hljs-string">'this is FAC'</span>);
  &#125;
&#125;

<span class="hljs-comment">//通过super关键字调用</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Famer</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Factory</span> </span>&#123;
  <span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">info</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">super</span>.run();
  &#125;
&#125;

<span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">main</span>(<span class="hljs-params"></span>)</span> &#123;
  Child c = <span class="hljs-keyword">new</span> Child();
  print(c.name);
  Boy b = <span class="hljs-keyword">new</span> Boy(<span class="hljs-string">'tom'</span>, <span class="hljs-number">20</span>, <span class="hljs-string">'男'</span>);
  b.exec();
  Dog d = <span class="hljs-keyword">new</span> Dog();
  d.info();
  Famer f = <span class="hljs-keyword">new</span> Famer();
  f.info();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-19"><a href="https://juejin.cn/post/6943478965856108558"></a>多态</h5>
<blockquote>
<p>这里的多态可以通过继承、实现、mixins进行体现。</p>
</blockquote>
<h5 data-id="heading-20"><a href="https://juejin.cn/post/6943478965856108558"></a>封装</h5>
<blockquote>
<p>上面将类单独抽离出去经过import进行引入的过程就是封装的过程，</p>
</blockquote>
<h5 data-id="heading-21"><a href="https://juejin.cn/post/6943478965856108558"></a>抽象类</h5>
<blockquote>
<p>通过abstract进行定义抽象类,抽象类一般用于定义标准，抽象类不可以被实例化，只有被他继承的子类可以被实例化，如果子类继承类抽象类，就必须实现抽象类里面的方法<br>
定义一个抽象类 包含一个抽象方法 用于约束子类</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">abstract <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span> </span>&#123;
  eat();
  <span class="hljs-function"><span class="hljs-title">printInfo</span>(<span class="hljs-params"></span>)</span> &#123;
    print(<span class="hljs-string">'我是一个普通抽象类里面的普通方法'</span>);
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Animal</span> </span>&#123;
  @override
  <span class="hljs-function"><span class="hljs-title">eat</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// <span class="hljs-doctag">TODO:</span> implement eat</span>
    print(<span class="hljs-string">'my name is animal'</span>);
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Cat</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Animal</span> </span>&#123;
  @override
  <span class="hljs-function"><span class="hljs-title">eat</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// <span class="hljs-doctag">TODO:</span> implement eat</span>
    <span class="hljs-keyword">throw</span> UnimplementedError();
  &#125;
&#125;

<span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">main</span>(<span class="hljs-params"></span>)</span> &#123;
  Dog d = <span class="hljs-keyword">new</span> Dog();
  d.eat();
  d.printInfo();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-22"><a href="https://juejin.cn/post/6943478965856108558"></a>接口和实现</h4>
<blockquote>
<p>dart中没有interface关键字，我们一般使用类进行定义接口，常规的写法是使用抽象类进行接口的定义，通过implates进行实现，接口就是约定一些类的规范和方法，这里的接口可能和对java有深刻认知的人有点出入，java中定义接口是使用interface关键字进行定义一个类的，但是dart中是使用抽象类进行定义接口，当然你也可以使用普通的类进行定义接口</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">abstract <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Db</span> </span>&#123;
  <span class="hljs-built_in">String</span> uri; <span class="hljs-comment">//数据库的链接地址</span>
  add(); <span class="hljs-comment">//数据库的增加方法</span>
  del(); <span class="hljs-comment">//数据库的删除方法</span>
  update(); <span class="hljs-comment">//数据库的更新方法</span>
  search(); <span class="hljs-comment">//数据库的查询方法</span>
&#125;

abstract <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Language</span> </span>&#123;
  <span class="hljs-built_in">String</span> name;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Mysql</span> <span class="hljs-title">implements</span> <span class="hljs-title">Db</span> </span>&#123;
  @override
  <span class="hljs-built_in">String</span> uri;

  @override
  <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// <span class="hljs-doctag">TODO:</span> implement add</span>
    print(<span class="hljs-string">'this is mysql'</span>);
  &#125;

  @override
  <span class="hljs-function"><span class="hljs-title">del</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// <span class="hljs-doctag">TODO:</span> implement del</span>
    <span class="hljs-keyword">throw</span> UnimplementedError();
  &#125;

  @override
  <span class="hljs-function"><span class="hljs-title">search</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// <span class="hljs-doctag">TODO:</span> implement search</span>
    <span class="hljs-keyword">throw</span> UnimplementedError();
  &#125;

  @override
  <span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// <span class="hljs-doctag">TODO:</span> implement update</span>
    <span class="hljs-keyword">throw</span> UnimplementedError();
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Oracle</span> <span class="hljs-title">implements</span> <span class="hljs-title">Db</span> </span>&#123;
  @override
  <span class="hljs-built_in">String</span> uri;

  @override
  <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// <span class="hljs-doctag">TODO:</span> implement add</span>
    print(<span class="hljs-string">'this is oracle'</span>);
  &#125;

  @override
  <span class="hljs-function"><span class="hljs-title">del</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// <span class="hljs-doctag">TODO:</span> implement del</span>
    <span class="hljs-keyword">throw</span> UnimplementedError();
  &#125;

  @override
  <span class="hljs-function"><span class="hljs-title">search</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// <span class="hljs-doctag">TODO:</span> implement search</span>
    <span class="hljs-keyword">throw</span> UnimplementedError();
  &#125;

  @override
  <span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// <span class="hljs-doctag">TODO:</span> implement update</span>
    <span class="hljs-keyword">throw</span> UnimplementedError();
  &#125;
&#125;

<span class="hljs-comment">//实现多个接口的时候，要同时实现里面的方法</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Impl</span> <span class="hljs-title">implements</span> <span class="hljs-title">Db</span>, <span class="hljs-title">Language</span> </span>&#123;
  @override
  <span class="hljs-built_in">String</span> name;

  @override
  <span class="hljs-built_in">String</span> uri;

  @override
  <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// <span class="hljs-doctag">TODO:</span> implement add</span>
    <span class="hljs-keyword">throw</span> UnimplementedError();
  &#125;

  @override
  <span class="hljs-function"><span class="hljs-title">del</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// <span class="hljs-doctag">TODO:</span> implement del</span>
    <span class="hljs-keyword">throw</span> UnimplementedError();
  &#125;

  @override
  <span class="hljs-function"><span class="hljs-title">search</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// <span class="hljs-doctag">TODO:</span> implement search</span>
    <span class="hljs-keyword">throw</span> UnimplementedError();
  &#125;

  @override
  <span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// <span class="hljs-doctag">TODO:</span> implement update</span>
    <span class="hljs-keyword">throw</span> UnimplementedError();
  &#125;
&#125;

<span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">main</span>(<span class="hljs-params"></span>)</span> &#123;
  Mysql m = <span class="hljs-keyword">new</span> Mysql();
  m.add();
  Oracle o = <span class="hljs-keyword">new</span> Oracle();
  o.add();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-23"><a href="https://juejin.cn/post/6943478965856108558"></a>mixins</h4>
<blockquote>
<p>在dart中可以实现类似多继承的功能，但是他不是多继承，因为只可以单继承，多实现，mixins是一种新特性,但是喜欢vue的人可能就模糊了，vue中也有这个，但是那个是为了混入一些公共的方法，这里也可以这么理解，类的目的也是为了处理功能的一块代码，为了别的类也可以使用，根源是一样的。<br>
作为被mixins的类，不可以是继承的类，也就是说如果他已经继承类别的类，那么他就不可以被mixins了<br>
被minxin的类不可以有构造函数，如果有多个同样的方法的时候，with后面的函数会最后被执行，也就是最后的会替代前面的同名的函数<br>
子类可以继承父类同时进行mixins别的父类</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">printInfoA</span>(<span class="hljs-params"></span>)</span> &#123;
    print(<span class="hljs-string">'this is A'</span>);
  &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">B</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">printInfoB</span>(<span class="hljs-params"></span>)</span> &#123;
    print(<span class="hljs-string">'this is B'</span>);
  &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">D</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">D</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
  <span class="hljs-function"><span class="hljs-title">printInfoD</span>(<span class="hljs-params"></span>)</span> &#123;
    print(<span class="hljs-string">'this is D'</span>);
  &#125;
&#125;
<span class="hljs-comment">//可以实现继承和mixins同时使用</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">C</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">D</span> <span class="hljs-title">with</span> <span class="hljs-title">A</span>, <span class="hljs-title">B</span> </span>&#123;&#125;
<span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">main</span>(<span class="hljs-params"></span>)</span> &#123;
  C c = <span class="hljs-keyword">new</span> C();
  c.printInfoA();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-24"><a href="https://juejin.cn/post/6943478965856108558"></a>泛型</h4>
<blockquote>
<p>为了解决类，方法，接口，的复用性，以及对不特定类型的支持（数据校验），通过T【当然你也可以使用别的字母进行，只是我们默认使用的是T】关键字进行泛型的定义</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//定义一个泛型的方法</span>
T getData<T>(T value) &#123;
  <span class="hljs-keyword">return</span> value;
&#125;

<span class="hljs-comment">//定义一个泛型类</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PrintClass</span><<span class="hljs-title">T</span>> </span>&#123;
  List list = <span class="hljs-keyword">new</span> List<T>();
  <span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params">T value</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.list.add(value);
  &#125;

  <span class="hljs-function"><span class="hljs-title">printInfo</span>(<span class="hljs-params"></span>)</span> &#123;
    print(<span class="hljs-built_in">this</span>.list);
  &#125;
&#125;
<span class="hljs-comment">//可以动态的传入类型</span>
<span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">main</span>(<span class="hljs-params"></span>)</span> &#123;
  getData(<span class="hljs-string">'tom'</span>);
  getData<<span class="hljs-built_in">String</span>>(<span class="hljs-string">'jim'</span>);
  getData<int>(<span class="hljs-number">12</span>);
  <span class="hljs-comment">//List默认的就是泛型的类</span>
  List list = <span class="hljs-keyword">new</span> List<<span class="hljs-built_in">String</span>>();
  list.add(<span class="hljs-string">'jim'</span>);
  print(list);
  List list1 = <span class="hljs-keyword">new</span> List<int>();
  list1.add(<span class="hljs-number">123</span>);
  print(list1);

  PrintClass p = <span class="hljs-keyword">new</span> PrintClass();
  p.add(<span class="hljs-string">'1234'</span>);
  p.add(<span class="hljs-number">123</span>);
  p.printInfo();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-25"><a href="https://juejin.cn/post/6943478965856108558"></a>库</h4>
<blockquote>
<p>将一些公共的功能，单独抽离出来成一个文件，通过引入的方式进行使用的，就是一个库</p>
</blockquote>
<h5 data-id="heading-26"><a href="https://juejin.cn/post/6943478965856108558"></a>自定义库</h5>
<blockquote>
<p>根据路径进行引入</p>
</blockquote>
<h5 data-id="heading-27"><a href="https://juejin.cn/post/6943478965856108558"></a>系统内置的库</h5>
<blockquote>
<p>通过import ’dart:math‘</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">实例接口:https:<span class="hljs-comment">//news-at.zhihu.com/api/3/stories/latest</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-28"><a href="https://juejin.cn/post/6943478965856108558"></a>Pub包管理系统中的库（第三方库）</h5>
<blockquote>
<p>三个地址：htts://pub.dev/packages<br>
https://pub.flutter-io.cn/packages<br>
https://pub.dartlang.org/flutter/<br>
第一步：在项目中新建一个pubspec.yaml<br>
将里面的name，desc，dep写好</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">name:<span class="hljs-string">'enlish'</span>,
<span class="hljs-attr">description</span>:<span class="hljs-string">'描述信息'</span>,
<span class="hljs-attr">dependencies</span>:<span class="hljs-string">'去地址里面的install中找安装的版本信息'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>cd 到你的项目目录中，进行pub get命令进行安装第三方库<br>
引入的时候import ’package:math‘ ‘看地址example中的教程就可以’</p>
</blockquote>
<h4 data-id="heading-29"><a href="https://juejin.cn/post/6943478965856108558"></a>结尾</h4>
<blockquote>
<p>到此，Dart的基本介绍就结束了，Dart这门语言总体来说还是很容易接受的，毕竟学习的人一般不会java就会js，如果都会的话，就更加容易接受了，所以写的不是说很深入，只是简单的介绍一下，为学习flutter打下一些基础！</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            