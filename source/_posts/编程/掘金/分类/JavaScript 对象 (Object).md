
---
title: 'JavaScript 对象 (Object)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb07e6f59c2c46eaa66277f4e9eb1dea~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 09 Jul 2021 01:23:48 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb07e6f59c2c46eaa66277f4e9eb1dea~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">对象(Object)</h2>
<blockquote>
<p><strong>对象由花括号分隔，在括号内部，对象的属性以名称和值对的形式 (name : value) 来定义，也叫 json。</strong><br>
<strong>属性由逗号分隔，空格和折行无关紧要。声明可横跨多行。</strong></p>
</blockquote>
<blockquote>
<p>定义一个对象, 姓名：Keafmd, 年龄：18 ，地址：北京，isEdu:false</p>
</blockquote>
<p><strong>样例代码：</strong></p>
<pre><code class="copyable">var Ke = &#123;
    'name': 'Keafmd',
    'age': 18,
    address: '北京',
    isEdu:false
&#125;
console.log(Ke)

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>完整代码：</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title></title>
<script>
var Ke = &#123;
    'name': 'Keafmd',
    'age': 18,
    address: '北京',
    isEdu:false
&#125;
console.log(Ke)
</script>
</head>
<body>

</body>
</html>


<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果截图：</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb07e6f59c2c46eaa66277f4e9eb1dea~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">对象的创建</h2>
<h3 data-id="heading-2">使用 &#123;&#125; 创建</h3>
<pre><code class="copyable">var person = &#123;
    name : 'Keafmd',
    sayHi:function()&#123;
        console.log('hi, my name is :'+this.name)
    &#125;
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>样例代码：</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script>
var person = &#123;
    name : 'Keafmd',
    sayHi:function()&#123;
        console.log('hi, my name is :'+this.name)
    &#125;
&#125;;
console.log(person) 
person.sayHi()
</script>
<title></title>
</head>
<body>

</body>
</html>



<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果截图：</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5a287c4d75d4bfa9800ffaca670977c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">使用 Object 创建</h3>
<pre><code class="copyable">var p = new Object();
p.name = 'Keafmd';
p.age = 18;

console.log(p);

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>样例代码：</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script>
var p = new Object();
p.name = 'Keafmd';
p.age = 18;

console.log(p);
</script>
<title></title>
</head>
<body>
</body>
</html>


<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果截图：</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c43abf35fc54cf5a2c49c431cb84e77~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">使用 Function 创建</h3>
<pre><code class="copyable">function Student()&#123;
   this.name = '';
    this.age = 0;
&#125;

var stu1 = new Student();
stu1.name = "Keafmd";
stu1.age = 18;
stu1.address = '哈尔滨';

console.log(stu1);

var stu2 = new Student();
console.log(stu2);

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>样例代码：</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script>
function Student()&#123;
    this.name = '';
    this.age = 0;
&#125;

var stu1 = new Student();
stu1.name = "Keafmd";
stu1.age = 18;
stu1.address = '哈尔滨';

console.log(stu1);

var stu2 = new Student();
console.log(stu2);
</script>
<title></title>
</head>
<body>
</body>
</html>


<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果截图：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba6e36ec2f0a4181bccdc12e0e43cd9b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">使用 class 关键字</h3>
<pre><code class="copyable">class Human&#123;
   constructor(name) &#123;
        this.name = name;
    &#125;

    sayHi()&#123;
        console.log('我是： '+this.name);
    &#125;

&#125;

var  h1 = new Human('Keafmd');
h1.sayHi()

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>样例代码：</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script>
class Human&#123;
    constructor(name) &#123;
    this.name = name;
    &#125;

    sayHi()&#123;
        console.log('我是： '+this.name);
    &#125;

&#125;

var  h1 = new Human('Keafmd');
h1.sayHi()
</script>
<title></title>
</head>
<body>
</body>
</html>


<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果截图：</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9b45169090e4434b0c2bdb15143dd58~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">对象的原型模型</h2>
<blockquote>
<p><strong>通过对象可以给对象扩展字段（属性、方法）<br>
如果想同一个类型，都添加属性，则需要用到原型 prototype</strong></p>
</blockquote>
<p><strong>样例代码：</strong></p>
<pre><code class="copyable"><!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
        <script>
            function Student()&#123;
                this.name = '';
                this.age = 0;
            &#125;

            var  s1 = new Student();

            
            
            
            

            
            Student.prototype.sayHi = function()&#123;
                console.log('打招呼')
            &#125;

            s1.sayHi();


            var  s2 = new Student();
            s2.sayHi();
        </script>
    </head>
    <body>
    </body>
</html>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>效果截图：</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/913e722bf4944e4ba0ee72c6811c6666~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><br>
<strong>写作不易，读完如果对你有帮助，感谢点赞支持！<br>
如果你是电脑端，看见右下角的 “一键三连” 了吗，没错点它 [哈哈]</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9a19b8514aa44d183f921cc3593262c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>加油！</strong></p>
<p><strong>共同努力！</strong></p>
<p><strong>Keafmd</strong></p></div>  
</div>
            