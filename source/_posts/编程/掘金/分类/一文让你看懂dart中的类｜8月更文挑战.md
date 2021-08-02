
---
title: '一文让你看懂dart中的类｜8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4012'
author: 掘金
comments: false
date: Sat, 31 Jul 2021 20:37:23 GMT
thumbnail: 'https://picsum.photos/400/300?random=4012'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><h4 data-id="heading-0">dart是一门面向对象的语言</h4>
<pre><code class="copyable">dart是一门实用类和单继承的面向对象的语言
在dart中所有的对象都是类的实例。
所有的类都是Object的子类
类都是有属性和方法组成的
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">定义一个类</h4>
<pre><code class="copyable">在dart中，我们可以通过关键字class来定义类
类名通常首字母是你大写的。采用的是大驼峰的方式。
如果我们定的是函数或者方法。我们首字母是小写的；采用小驼峰的方式
我们刚刚说了：类通常是由属性和方法组成的。下面我们就实现一个类
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">实现一个简单的类</h4>
<pre><code class="copyable">class PersonIno &#123;
  // 类中的属性
  String name = '林漾';
  int age = 30;
  // 类中的方法
  likes() &#123;
    print('喜欢逛街');
  &#125;

  // 访问类中的属性
  info() &#123;
    // 直接访问属性
    print('我叫 $name,今年$age');

    // 通过this的来访问属性
    print('我叫 $&#123;this.name&#125;,今年$&#123;this.age&#125;');
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">使用类之前进行实例化</h4>
<pre><code class="copyable">void main() &#123;
  //实例化
  var p = new PersonIno();
  //调用类中的方法
  p.info();
  print(p.name);

  // 我们也可以声明这个p的类型哈;PersonIno类型
  PersonIno p1 = new PersonIno();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">dart中的构造函数</h4>
<pre><code class="copyable">class PersonIno &#123;
  // 类中的属性
  String name = '林漾';
  int age = 30;

  // 构造函数的名称和类型相同
  PersonIno() &#123;
    print('我是构造函数，在实例化的时候就会被触发');
  &#125;

  // 类中的方法
  likes() &#123;
    print('喜欢逛街');
  &#125;

  // 访问类中的属性
  info() &#123;
    // 直接访问属性
    print('我叫 $name,今年$age');

    // 通过this的来访问属性
    print('我叫 $&#123;this.name&#125;,今年$&#123;this.age&#125;');
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">使用构造函数初始化值</h4>
<pre><code class="copyable">我们现在的这个PersonIno类；
只能够输出一个人的信息和年龄
如果我们需要输出张三 李四  王五....
很多人的信息怎么办？？
这个时候我们就可以使用构造函数哈！
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">void main() &#123;
  //实例化
  var p = new PersonIno('李四', 20);
  p.info();
  
  // 类是可以被多次实例化的
  var p1 = new PersonIno('王五', 25);
  p1.info();
&#125;

class PersonIno &#123;
  // 类中的属性
  String name;
  int age;

  // 构造函数的名称和类型相同
  PersonIno(String name, int age) &#123;
    this.name = name;
    this.age = age;
  &#125;

  // 访问类中的属性
  info() &#123;
    // 通过this的来访问属性
    print('我叫 $&#123;this.name&#125;,今年$&#123;this.age&#125;');
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">简写dart中的构造函数</h4>
<pre><code class="copyable">  // 构造函数的简写方式
  PersonIno(this.name, this.age);

  // 与上面的相同
  PersonIno(String name, int age) &#123;
  this.name = name;
  this.age = age;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">命名构造函数。</h4>
<pre><code class="copyable">void main() &#123;
  //实例化
  var p = new PersonIno('李四', 20);
&#125;

class PersonIno &#123;
  // 类中的属性
  String name;
  int age;

  // 构造函数的简写方式
  PersonIno(this.name, this.age);
  PersonIno.myFun() &#123;
    print('我是命名的构造函数');
  &#125;
&#125;

我们都知道在实例化的时候，会默认触发【构造函数】。
但是并不会去触发【命名构造函数】哈
如何去触发【命名构造函数呢】
//这样就会触发默认的构造函数了
var p = new PersonIno.myFun();

一个类中只能有一个构造构造函数。
但是可以有多个构造函数
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">命名构造函数也可以初始化值</h4>
<pre><code class="copyable">void main() &#123;
  //实例化
  var p = new PersonIno.myFun('余声声', 22);
  p.info();
&#125;

class PersonIno &#123;
  // 类中的属性
  String name;
  int age;

  // 构造函数的简写方式
  PersonIno(this.name, this.age);
  PersonIno.myFun(this.name, this.age);
  // 访问类中的属性
  info() &#123;
    // 通过this的来访问属性
    print('我叫 $&#123;this.name&#125;,今年$&#123;this.age&#125;');
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">将类抽离出去</h4>
<pre><code class="copyable">在实际的开发中，我们可能会有很多的类。
这样会文件越来越大。导致维护麻烦
这个时候，我们就需要将类抽离出去
那么，如何将类抽离出去呢？？
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">在项目的根目录下创建一个文件夹lib.
将类放入这个文件夹下哈
文件名【PersonIno】和类名【PersonIno】相同

import 'lib/PersonIno.dart';
void main() &#123;
  //实例化
  var p = new PersonIno.myFun('余声声', 22);
  p.info();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">私有的方法和属性</h4>
<pre><code class="copyable">dart和其他的面向对象的语言不一样。
dart中没有public private  protected这些访问修饰符
但是我们可以使用_把一个属性或者方法定义成为一个私有的。
需要注意的是:
如果你在属性或者方法前面添加"_"在同一个文件送仍然是可以访问的【1】
但是如果是单独抽离出去的文件在属性和方法前面添加“_"就不可以访问【2】
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">举个例子【1】</h4>
<pre><code class="copyable">void main() &#123;
  var p = new PersonInfo('唐三', 18);
  print(p._age); //输出18是可以访问的
&#125;

class PersonInfo &#123;
  String name;
  int _age; //虽然添加了"_"表示私有，但是在同一个文件中仍然可以访问
  PersonInfo(this.name, this._age);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">例子【2】 lib目录下的 PersonInfo 类文件PersonInfo.dart</h4>
<pre><code class="copyable">class PersonIno &#123;
  // 类中的属性
  String _name;
  int age;

  // 构造函数的简写方式
  PersonIno(this._name, this.age);
  // 访问类中的属性
  info() &#123;
    // 通过this的来访问属性
    print('我叫 $&#123;this._name&#125;,今年$&#123;this.age&#125;');
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">这个时候就会出现访问报错</h4>
<pre><code class="copyable">import 'lib/PersonIno.dart';
void main() &#123;
  var p = new PersonIno('唐三', 18);
  print(p._name);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">求两个数字的和</h4>
<pre><code class="copyable">void main() &#123;
  Sun c = new Sun(10, 20);
  print(c.backSum());
&#125;

class Sun &#123;
  num a;
  num b;
  Sun(this.a, this.b);
  backSum() &#123;
    return this.a + this.b;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">使用getter求两个数字的和</h4>
<pre><code class="copyable">void main() &#123;
  Sun c = new Sun(10, 20);
  print(c.backSum); //直接访问属性的方式
&#125;

class Sun &#123;
  num a;
  num b;
  Sun(this.a, this.b);
  // 使用getter去掉小括号
  get backSum&#123;
    return this.a + this.b;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">setter方法的使用</h4>
<pre><code class="copyable">void main() &#123;
  Sun c = new Sun(10, 20);
  c.restateA = 100; //重新设置一个值
  print(c.backSum); //直接访问属性的方式 返回120
&#125;

class Sun &#123;
  num a;
  num b;
  Sun(this.a, this.b);
  // 使用getter去掉小括号
  get backSum &#123;
    return this.a + this.b;
  &#125;

  // setter的使用方法，
  set restateA(value) &#123;
    this.a = value;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            