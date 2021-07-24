
---
title: 'angular-组件传值'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7515'
author: 掘金
comments: false
date: Fri, 23 Jul 2021 02:52:38 GMT
thumbnail: 'https://picsum.photos/400/300?random=7515'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">子组件获取父组件数据和方法</h1>
<pre><code class="hljs language-js copyable" lang="js"><!-- 子组件 form -->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">app-form</span> [<span class="hljs-attr">shows</span>]=<span class="hljs-string">"shows"</span> [<span class="hljs-attr">run</span>]=<span class="hljs-string">"run"</span> [<span class="hljs-attr">news</span>]=<span class="hljs-string">"this"</span>></span>form 组件<span class="hljs-tag"></<span class="hljs-name">app-form</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>**</p>
<pre><code class="copyable"><!-- 父组件中定义 run 方法 -->
run()&#123;
    alert('父组件方法')
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在父组件中挂载子组件,通过绑定属性的方法绑定传递给子组件的数据(属性,方法,包括父组件本身)<br>
run是传递给子组件的方法,注意不要加()</p>
<p>**</p>
<pre><code class="copyable">import &#123; Component, OnInit,Input &#125; from '@angular/core';
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在子组件中引入 Input 模块</p>
<p>**</p>
<pre><code class="copyable">export class FormComponent implements OnInit &#123;

  @Input() shows:boolean
  @Input() run:any
  @Input() news:this

  constructor() &#123; &#125;
  ngOnInit(): void &#123;
  &#125;

  getrun()&#123;
    this.run()
    alert(this.news.title)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在子组件类中通过 @Input 装饰器接收父组件传递过来的数据(属性,方法,包括父组件本身)</p>
<p>**</p>
<pre><code class="copyable"><button (click)="getrun()">执行父组件方法</button>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>子组件中定义方法执行父组件传递过来的方法</p>
<h1 data-id="heading-1">父组件获取子组件数据和方法</h1>
<p>**</p>
<pre><code class="copyable"><app-form #formId>form 组件</app-form>
public msg = '子组件的一个msg'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在子组件挂载处定义个名称或者id,且定义一个获取数据和执行方法的事件</p>
<p>**</p>
<pre><code class="copyable">@ViewChild('formId') form: any
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过@ViewChild接受子组件传递过来的数据和方法</p>
<p>**</p>
<pre><code class="copyable">父组件中定义个方法
<button (click)="getchildMsg()">获取form子组件的msg</button>
<button (click)="getchildRun()">执行form子组件的方法</button>
 getchildMsg() &#123;
    alert(this.form.msg)
  &#125;
 getchildRun()&#123;
    this.form.formrun()
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行父组件中的事件就可以获得子组件的数据和方法</p>
<h1 data-id="heading-2">通过Output和EventEmitter</h1>
<p>**</p>
<pre><code class="copyable">import &#123; Component, OnInit, Output, EventEmitter &#125; from '@angular/core';
<span class="copy-code-btn">复制代码</span></code></pre>
<p>子组件中引入Output和EventEmitter</p>
<p>**</p>
<pre><code class="copyable"><button (click)="setrun()">通过@Output执行父组件数据</button>

@Output() private out = new EventEmitter()

setrun()&#123;
    alert(this.out.emit('子组件的数据'))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>子组件中定义方法,通过@Output()声明一个变量<br>
子组件中实例化 EventEmitter<br>
子组件中setrun是要执行的方法</p>
<p>**</p>
<pre><code class="copyable"><app-form (out)="run($event)">form 组件</app-form>
run(e) &#123;
  console.log(e)
  alert('父组件方法')
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>父组件中定义一个方法接收,父组件中的run方法接收的就是子组件的方法执行时传递给父组件的数据</p></div>  
</div>
            