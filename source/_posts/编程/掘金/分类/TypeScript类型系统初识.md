
---
title: 'TypeScript类型系统初识'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1170'
author: 掘金
comments: false
date: Sat, 14 Aug 2021 00:26:17 GMT
thumbnail: 'https://picsum.photos/400/300?random=1170'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第11天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">什么是类型系统</h2>
<p>类型系统包含两个重要组成部分：</p>
<ul>
<li>类型标注（定义、注解） - typing</li>
<li>类型检测（检查） - type-checking</li>
</ul>
<h3 data-id="heading-1">类型标注</h3>
<p>类型标注就是在代码中给数据（变量、函数（参数、返回值））添加类型说明，当一个变量或者函数（参数）等被标注以后就不能存储或传入与标注类型不符合的类型有了标注，TypeScript 编译器就能按照标注对这些数据进行类型合法检测。有了标注，各种编辑器、IDE等就能进行智能提示</p>
<p>在 TypeScript 中，类型标注的基本语法格式为：</p>
<pre><code class="copyable">数据载体:类型
let num:number = 100;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">类型检测</h3>
<p>顾名思义，就是对数据的类型进行检测。注意这里，重点是类型两字。类型系统检测的是类型，不是具体值（虽然，某些时候也可以检测值），比如某个参数的取值范围（1-100之间），我们不能依靠类型系统来完成这个检测，它应该是我们的业务层具体逻辑，类型系统检测的是它的值类型是否为数字！</p>
<h2 data-id="heading-3">基础简单的类型标注</h2>
<ul>
<li>基础类型</li>
<li>空和未定义类型</li>
<li>对象类型</li>
<li>数组类型</li>
<li>元组类型</li>
<li>枚举类型</li>
<li>无值类型</li>
<li>Never类型</li>
<li>任意类型</li>
<li>未知类型（Version3.0 Added）</li>
</ul>
<h3 data-id="heading-4">基础类型</h3>
<p>基础类型包含：string，number，boolean
标注的语法：</p>
<pre><code class="copyable">let title: string = 'TypeScript类型系统初识';
let num: number = 100;
let isOk: boolean = true;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">空和未定义类型</h3>
<p>因为在 Null 和 Undefined 这两种类型有且只有一个值，在标注一个变量为 Null 和 Undefined 类型，那就表示该变量不能修改了</p>
<pre><code class="copyable">let a: null;
a = null;// ok
a = 1;// error
<span class="copy-code-btn">复制代码</span></code></pre>
<p>默认情况下 null 和 undefined 是所有类型的子类型。 就是说你可以把 null 和 undefined 其它类型的变量</p>
<pre><code class="copyable">let a: number;
a = null;// ok
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果一个变量声明了，但是未赋值，那么该变量的值为 undefined，但是如果它同时也没有标注类型的话，默认类型为 any，any 类型后面有详细说明</p>
<pre><code class="copyable">// 类型为 `number`，值为 `undefined`
let a: number;
// 类型为 `any`，值为 `undefined`
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>小技巧1：指定 strictNullChecks 配置为 true，可以有效的检测 null 或者 undefined，避免很多常见问题，也可以使我们程序编写更加严谨</strong></p>
<p><strong>小技巧2：获取元素的方法返回的类型可能会包含 null，所以最好是先进行必要的判断，再进行操作</strong></p>
<h3 data-id="heading-6">对象类型</h3>
<h4 data-id="heading-7">内置对象类型</h4>
<p>在 JavaScript 中，有许多的内置对象，比如：Object、Array、Date……，我们可以通过对象的 构造函数 或者 类 来进行标注</p>
<pre><code class="copyable">let a: object = &#123;&#125;;
let arr: Array<number> = [1,2,3]; // 数组这里标注格式有点不太一样，后面我们在数组标注中进行详细讲解
let d1: Date = new Date();
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">自定义对象类型</h4>
<p>另外一种情况，许多时候，我们可能需要自定义结构的对象。这个时候，我们可以：</p>
<ul>
<li>字面量标注</li>
<li>接口</li>
<li>定义类或构造函数</li>
</ul>
<p>字面量标注：</p>
<pre><code class="copyable">let a: &#123;username: string; age: number&#125; = &#123;  
    username: '韩雷雷',  
    age: 35
&#125;;
// ok
a.username;
a.age;
// error
a.gender;

优点：方便直接
缺点：不利于维护和复用
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接口：</p>
<pre><code class="copyable">// 这里使用了 interface 关键字，在后面的接口章节中会详细讲解
interface Person &#123;  
    username: string;  
    age: number;
&#125;;
let a: Person = &#123;  
    username: '韩雷雷',  
    age: 35
&#125;;
// ok
a.username;
a.age;
// error
a.gender;

优点： 复用性高
缺点：接口只能作为类型标注使用，不能作为具体值，它只是一种抽象的结构定义，并不是实体，没有具体功能实现
<span class="copy-code-btn">复制代码</span></code></pre>
<p>构造函数：</p>
<pre><code class="copyable">class Person &#123; 
    constructor(public username: string, public age: number) &#123; 
    &#125;
&#125;
// ok
a.username;
a.age;
// error
a.gender;


优点：功能相对强大，定义实体的同时也定义了对应的类型
缺点：复杂，比如只想约束某个函数接收的参数结构，没有必要去定一个类，使用接口会更加简单
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">扩展</h4>
<p>包装对象：这里说的包装对象其实就是 JavaScript 中的 String、Number、Boolean，我们知道 string 类型 和 String 类型并不一样，在 TypeScript 中也是一样</p>
<pre><code class="copyable">let a: string;
a = '1';
// error String有的，string不一定有（对象有的，基础类型不一定有）
a = new String('1');
let b: String;
b = new String('2');
// ok 和上面正好相反b = '2';
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">数组类型</h3>
<p>TypeScript 中数组存储的类型必须一致，所以在标注数组类型的时候，同时要标注数组中存储的数据类型</p>
<h4 data-id="heading-11">泛型标注</h4>
<pre><code class="copyable">// <number> 表示数组中存储的数据类型，
let arr1: Array<number> = [];
// ok
arr1.push(100);
// error
arr1.push('Toney');
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">简单标注</h4>
<pre><code class="copyable">let arr2: string[] = [];
// ok
arr2.push('Toney');
// error
arr2.push(1);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">元祖类型</h3>
<p>元组类似数组，但是存储的元素类型不必相同，但是需要注意：</p>
<ul>
<li>初始化数据的个数以及对应位置标注类型必须一致-</li>
<li>越界数据必须是元组标注中的类型之一（标注越界数据可以不用对应顺序 - 联合类型</li>
</ul>
<pre><code class="copyable">let data1: [string, number] = ['Kobe Bryant', 100];
// ok
data1.push(100);
data1.push('YaoMing');
// error
data1.push(true);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">枚举类型</h3>
<p>枚举的作用组织收集一组关联数据的方式，通过枚举我们可以给一组有关联意义的数据赋予一些友好的名字</p>
<pre><code class="copyable">enum HTTP_CODE &#123;  
    OK = 200,  
    NOT_FOUND = 404,  
    METHOD_NOT_ALLOWED
&#125;;
// 200
HTTP_CODE.OK;
// 405
HTTP_CODE.METHOD_NOT_ALLOWED;
// error
HTTP_CODE.OK = 1;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意事项：</p>
<ul>
<li>key 不能是数字</li>
<li>value 可以是数字，称为 数字类型枚举，也可以是字符串，称为 字符串类型枚举，但不能是其它值，默认为数字：0</li>
<li>枚举值可以省略，如果省略，则：
<ul>
<li>第一个枚举值默认为：0</li>
<li>非第一个枚举值为上一个数字枚举值 + 1</li>
</ul>
</li>
<li>枚举值为只读（常量），初始化后不可修改</li>
</ul>
<h4 data-id="heading-15">字符串类型的枚举</h4>
<p>枚举类型的值，也可以是字符串类型</p>
<pre><code class="copyable">enum URLS &#123;  
    USER_REGISETER = '/user/register',  
    USER_LOGIN = '/user/login',  
    // 如果前一个枚举值类型为字符串，则后续枚举项必须手动赋值  INDEX = 0
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意事项：</p>
<ul>
<li>如果前一个枚举值类型为字符串，则后续枚举项必须手动赋值</li>
</ul>
<p><strong>小技巧：枚举名称可以是大写，也可以是小写，推荐使用全大写（通常使用全大写的命名方式来标注值为常量）</strong></p>
<h3 data-id="heading-16">无值类型</h3>
<p>表示没有任何数据的类型，通常用于标注无返回值函数的返回值类型，函数默认标注类型为：void</p>
<pre><code class="copyable">function fn():void &#123; 
    // 没有 return 或者 return undefined
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在 strictNullChecks 为 false 的情况下，undefined 和 null 都可以赋值给 void</li>
<li>但是当 strictNullChecks 为 true 的情况下，只有 undefined 才可以赋值给 void</li>
</ul>
<h3 data-id="heading-17">Never类型</h3>
<p>当一个函数永远不可能执行 return 的时候，返回的就是 never ，与 void 不同，void 是执行了 return， 只是没有值，never 是不会执行 return，比如抛出错误，导致函数终止执行</p>
<pre><code class="copyable">function fn(): never &#123; 
    throw new Error('error');
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">任意类型</h3>
<p>有的时候，我们并不确定这个值到底是什么类型或者不需要对该值进行类型检测，就可以标注为 any 类型</p>
<pre><code class="copyable">let a: any;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>一个变量申明未赋值且未标注类型的情况下，默认为 any 类型</li>
<li>任何类型值都可以赋值给 any 类型</li>
<li>any 类型也可以赋值给任意类型</li>
<li>any 类型有任意属性和方法</li>
</ul>
<p>注意：标注为 any 类型，也意味着放弃对该值的类型检测，同时放弃 IDE 的智能提示</p>
<p><strong>小技巧：当指定 noImplicitAny 配置为 true，当函数参数出现隐含的 any 类型时报错</strong></p>
<h3 data-id="heading-19">未知类型</h3>
<p>unknow，3.0 版本中新增，属于安全版的 any，但是与 any 不同的是：、</p>
<ul>
<li>unknow 仅能赋值给 unknow、any</li>
<li>unknow 没有任何属性和方法</li>
</ul>
<h3 data-id="heading-20">函数类型</h3>
<p>在 JavaScript 函数是非常重要的，在 TypeScript 也是如此。同样的，函数也有自己的类型标注格式</p>
<ul>
<li>参数</li>
<li>返回值</li>
</ul>
<pre><code class="copyable">函数名称( 参数1: 类型, 参数2: 类型... ): 返回值类型;

function add(x: number, y: number): number &#123; 
    return x + y;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">结语</h2>
<p>我是刚开始学习TypeScript的小白，关于TypeScript的一些文章，只是我闲暇之时复习一下，同时整理出来笔记，加深自己的印象，也希望能帮助一下跟我一样是初学TypeScript的同学，同时也希望大佬多多点评！！！</p></div>  
</div>
            