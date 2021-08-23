
---
title: 'js-函数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6808'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 02:13:42 GMT
thumbnail: 'https://picsum.photos/400/300?random=6808'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>一、函数的介绍</p>
<p>js函数语法 ：function 函数名()&#123;&#125;</p>
<p>1、function 是预定义 函数名是自定义的 ，函数名的定义规则符合 变量的定义规则</p>
<p>2、数字（在后面） 字母 下划线 $ 符号 组成，定义一个函数名为fn的函数，这个函数可以理解成是一个箱子可以装代码，代码会被装在 大括号里面，装起来之后是代码是不会执行的。</p>
<p>二、函数的调用
1、例如function fn()&#123;&#125;;   可以在函数外面直接调用fn();fn()中的函数执行一遍</p>
<p>2、函数之间也可以调用</p>
<pre><code class="copyable">    function fn1()&#123;
            console.log(111);
            fn2();
        &#125;
        function fn2()&#123;
            console.log(222);
        &#125;
        fn1();//输出结果是111 222
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、函数的事件调取</p>
<p>1.通过标签.onclick =  未执行的函数 （匿名函数）</p>
<p>2.通过行间的onclick属性 执行函数 ，注意需要小括号 （可以传参数）</p>
<pre><code class="copyable">  <button id="btn" onclick="fn(1,2)">按钮</button>//
    //第一种
    btn.onclick = function()&#123;
          console.log("函数执行了");
        &#125;
        
    //第二种
  function fn(a,b)&#123;

            console.log("fn",a,b);

        &#125;

        // var fn = function()&#123;

        //     console.log("fn");

        // &#125;

        // btn.onclick = fn;  //当点击按钮的时候执行  fn函数；
<span class="copy-code-btn">复制代码</span></code></pre>
<p>三、定义函数的方式
1、声明型，函数的调用可以再定义之前 也可以在定义之后</p>
<p>函数定义方式一：命名函数（声明式）</p>
<pre><code class="copyable">function fn()&#123;  

            console.log(1111);

        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、赋值型，赋值式函数的调用只能在函数定义之后调用，如果在函数定义之前调用那么就会报错</p>
<p>函数定义的第二种方式： 匿名函数（赋值式）</p>
<pre><code class="copyable">var fn = function()&#123;  

            console.log(123);

        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>四、函数的参数</p>
<p>形参、实参、隐藏参数，参数可以写多个，并且是一一对应的关系</p>
<pre><code class="copyable">function fn(a)&#123;  //a是形参

            console.log(a);

        &#125;
        fn(1);//1是实参
<span class="copy-code-btn">复制代码</span></code></pre>
<p>隐藏参数：</p>
<pre><code class="copyable"> // 隐藏参数 ： 处理不定参数问题 ;

        function fn()&#123;  //一个形参都不写 

                // 在 js函数里会提供一个隐藏参数 会把所有传入的参数当成伪数组（长的像数组，使用上有点区别 ，我们在这就可以简单理解成是数组）

                // 隐藏参数是预定义的 arguments 

                console.log(arguments.length);  //是隐藏参数

        &#125;

        // fn函数调用的时候 实参 可以有2个参数传入 也可能有三个传入还有可能有很多个参数传入，

        // fn(1);

        fn(1,'hello');

        fn(1,2,3);

        fn(1,2,3,4,5);


        // 总结：arguments 是隐藏参数 ，会把传入的实参放在伪数组里 ； 一般是处理不定参的问题

        // 如果不是不定参的问题 不建议频繁使用arguments （可读性差）
<span class="copy-code-btn">复制代码</span></code></pre>
<p>数组：</p>
<pre><code class="copyable">        var array=[1,2,3]//1是该数组的第0个键值，2是第1位，3是第二位，
        //3也可以用数组的长度减1获取
        console.log(array.length);//获取数组长度
<span class="copy-code-btn">复制代码</span></code></pre>
<p>数组的循环：</p>
<pre><code class="copyable">        var array=[1,2,3];
        for(i=0;i<array.length;i++)&#123;//从0开始循环，判断条件小于数组长度
            console.log(array[i])
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>字符串数组：</p>
<pre><code class="copyable">    var str="abc123";
        var newStr="";
        var str0=str[0];
        var strLast=str.length-1;
        for(i=0;i<str.length;i++)&#123;
            if(i!=0&&i!=str.length-1)&#123;
                newStr+=str[i]
            &#125;
        &#125;
        console.log("原来的字符串"+str);
        console.log("新的字符串"+newStr);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数return的使用:
1.阻止函数中后续代码的执行(函数里return之后的代码没有任何意义)  2. 返还函数里的值</p>
<pre><code class="copyable">    function fn(a)&#123;
           console.log(a);
           return a;//可以返回任何类型
       &#125;
       fn(1);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数的优点：1. 封装 （把函数保存起来） 2.复用 3.延迟执行 ；</p>
<p>变量提升与函数提升:</p>
<p>1.变量提升只会提升变量名的声明，而不会提升变量的赋值初始化。</p>
<p>2.函数提升的优先级大于变量提升的优先级，即函数提升在变量提升之上。</p>
<pre><code class="copyable"> console.log(a);  // a 是啥？ 1. undefined 2.报错

        // 结果是 undefined  有点不符合逻辑

        if(false)&#123;

            var a = 10;

        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>五、函数的作用域:
全局作用域：自己定义的全局变量 js会把它放在 预定义的全局变量上，js里全局内置的变量是window
局部作用域(函数作用域) :一个函数包裹的区域 ，被称为函数作用域 ，也是局部作用域</p>
<pre><code class="copyable">    var a=1;//全局作用域
       function fn()&#123;
           var a=2;//局部作用域
           console.log(a);
       &#125;
       fn();//执行a=2;作用域从内到外
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            