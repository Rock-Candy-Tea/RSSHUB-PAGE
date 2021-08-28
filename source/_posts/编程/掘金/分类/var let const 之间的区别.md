
---
title: 'var let const 之间的区别'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4337'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 06:46:19 GMT
thumbnail: 'https://picsum.photos/400/300?random=4337'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">通常面试的时候 都会让说说 var let const 这3者的区别</h3>
<h4 data-id="heading-1">今天我们来说说它的区别</h4>
<p>以前我基本都是说都是用来声明对象的<br>
只是const有些特殊 它声明的对象 值不能“更改”<br>
当然 这里的"更改"指的是 string 和 number 类型
array 和 obj 除外</p>
<pre><code class="copyable">&#123;
    let a = "let definde a";
    var b = "var definde b";
    const c = "const dedinde c";
&#125;


console.log(a);  // a is not dedine
console.log(b);  // var definde b
console.log(c);  // c is not dedine
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先看下上面的值输出<br>
只有 var 定义的变量 能在外部获取到，let 和 const 出了&#123;&#125;作用域外， 就没办法获取到
let 和 const 只有在声明的作用域内才能读取到</p>
<p>很多时候，我们都会通过</p>
<pre><code class="copyable">    if(typeof a === 'undefined')&#123;
         再进行逻辑处理
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是 以上这种情况只能是在用 var 声明变量的情况下不会出问题
因为 var 会出现变量提升</p>
<p>下面通过 var let const 来声明一个变量 然后在声明的上面打印它</p>
<pre><code class="copyable">    console.log(a)
    var a = 1;
    
    console.log(a)
    let a = 1;

    console.log(a)
    const a = 1;
    
    分别得到的是
    undefined
    报错 ：Cannot access 'a' before initialization
    报错 ：Cannot access 'a' before initialization
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而在let 和 const 这两种情况下 <br>
在没有声明变量之前，是无法获取变量 <br>
typeof 判断 undefined 就失去了意义</p>
<pre><code class="copyable">       所以 很多时候 要改变写写法规范了
       try&#123;
            console.log(a);
        &#125;catch(e)&#123;
            console.log("a 不存在",e)
        &#125;
        const a = 1;
        let a = 1;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来就是都两者都存在的情况下</p>
<pre><code class="copyable">            var b = 2;
            if(b)&#123;
                b = 3;
                console.log(b); //报错 ：Cannot access 'a' before initialization

                let b = 1;
                console.log(b); //1

                b = 3;
                console.log(b);//3
            &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>只要在块级作用域内 声明的变量 那它所在的作用域内 不受外部声明相同变量的影响 <br>
它所在的作用域 在它声明之前都是 无法访问的<br>
这种现象属于暂时性死区</p>
<p>这里 有个好玩的东西<br>
在for 循环里， 我通过let 声明了变量 index<br>
在循环里我 再通过 let 再次声明index</p>
<pre><code class="copyable">        通常情况下
        如果 在同一作用域内

        var 声明变量
        var a=1;
        var a=2;
        consloe.log(a); //2

        但是用 let 同样的声明
        consloe.log(a);//Identifier 'a' has already been declared
        它会报个错误，提示你已经声明过了

        但接下来 for循环却 打印了 3次 没出想上面的报错
        for (let index = 0; index < 3; index++) &#123;
            let index = "index";
            console.log(index);// index index index
        &#125;
        
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里 我们可以把 for 看成 父子 作用域 for（这里 声明的属于 父）&#123; 这里声明的属于子 &#125;<br>
他们都作用于两个不同的作用域 ，所以不会报错</p>
<h3 data-id="heading-2">通过这些 有没有给到你一丝丝的眼前一亮呢</h3></div>  
</div>
            