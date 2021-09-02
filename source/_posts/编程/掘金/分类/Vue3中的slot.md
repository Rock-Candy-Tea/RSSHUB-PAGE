
---
title: 'Vue3中的slot'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7516'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 03:17:27 GMT
thumbnail: 'https://picsum.photos/400/300?random=7516'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>小编今天和大家一起探讨Vue中的插槽(slot)的概念，熟悉Vue的小伙伴都知道父子组件之间可以相互传递数据，但是传递DOM结构的时候，再通过属性的方式就有些麻烦，我们先来看个父子组件的例子。大家还可以关注我的微信公众号，蜗牛全栈。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> app= Vue.createApp(&#123;    
    <span class="hljs-attr">template</span>: <span class="hljs-string">`<myform />`</span>
&#125;)
app.component(<span class="hljs-string">'myform'</span>,&#123;    
    <span class="hljs-attr">methods</span>:&#123;        
        <span class="hljs-function"><span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>)</span>&#123;            
            alert(<span class="hljs-string">'handleClick'</span>)        
        &#125;    
    &#125;,    
    <span class="hljs-attr">template</span>: <span class="hljs-string">`<div>
                    <input />        
                    <button @click="handleClick">提交</button>    
                </div>`</span>&#125;)
<span class="hljs-keyword">const</span> vm = app.mount(<span class="hljs-string">"#root"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面是一个最基本的父子引用的例子，在父组件中使用的是类似h5中input单标签，有的时候我们会有这样的需求，对于上面的提交，我们有的时候希望渲染成一个按钮，有的时候我们只是希望渲染成普通div。这个时候slot就显示出威力了，我们可以把代码写成这样</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> app= Vue.createApp(&#123;    
<span class="hljs-comment">// 将原来的单标签修改为双标签，标签之间的内容会替换掉子组件中的<slot></slot></span>
    <span class="hljs-attr">template</span>: <span class="hljs-string">`<myform>                
                    <div>提交</div>              
                </myform>              
                <myform>                
                    <button>提交</button>              
                </myform>`</span>
&#125;)
app.component(<span class="hljs-string">'myform'</span>,&#123;    
    <span class="hljs-attr">methods</span>:&#123;        
        <span class="hljs-function"><span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>)</span>&#123;            
            alert(<span class="hljs-string">'handleClick'</span>)        
        &#125;    
    &#125;,    
    <span class="hljs-comment">// 不能在slot直接添加@click方式，可以在外面添加span标签    </span>
    <span class="hljs-attr">template</span>: <span class="hljs-string">`<div>        
                <input />        
                <span @click="handleClick">            
                    <slot></slot>        
                </span>    
            </div>`</span>
&#125;)
<span class="hljs-keyword">const</span> vm = app.mount(<span class="hljs-string">"#root"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实对于slot，我们肯定不能仅仅满足于此，有的时候也需要进行数据绑定，对于父子组件，遵循的就是父组件中父组件绑定数据，子组件中子组件绑定数据。不会相互混淆</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> app= Vue.createApp(&#123;    
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;        
        <span class="hljs-keyword">return</span> &#123;            
            <span class="hljs-attr">f_data</span>:<span class="hljs-string">'1234'</span>        
        &#125;    
&#125;,    
<span class="hljs-attr">template</span>: <span class="hljs-string">`<myform>                
                <test />            
            </myform>            
            <myform>                
                &#123;&#123; f_data &#125;&#125;            
            </myform>`</span>&#125;)
app.component(<span class="hljs-string">'myform'</span>,&#123;    
    <span class="hljs-attr">methods</span>:&#123;        
        <span class="hljs-function"><span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>)</span>&#123;            
            alert(<span class="hljs-string">'handleClick'</span>)        
        &#125;    
    &#125;,    
    <span class="hljs-attr">template</span>: <span class="hljs-string">`<div>        
                    <input />        
                    <span @click="handleClick">            
                        <slot></slot>        
                    </span>    
                </div>`</span>
    &#125;)
app.component(<span class="hljs-string">'test'</span>,&#123;    
    <span class="hljs-attr">template</span>: <span class="hljs-string">`<div>        
                test component slot    
            </div>`</span>
    &#125;)
<span class="hljs-keyword">const</span> vm = app.mount(<span class="hljs-string">"#root"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在定义了slot之后，如果自定义组件之间什么也不传递的话，默认是空字符串，如果我们希望添加默认值的话，可以这样</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> app= Vue.createApp(&#123;
    <span class="hljs-attr">template</span>: <span class="hljs-string">`<myform></myform>`</span>
&#125;)
app.component(<span class="hljs-string">'myform'</span>,&#123;    
    <span class="hljs-attr">methods</span>:&#123;        
        <span class="hljs-function"><span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>)</span>&#123;            
            alert(<span class="hljs-string">'handleClick'</span>)        
        &#125;    
    &#125;,    
    <span class="hljs-attr">template</span>: <span class="hljs-string">`<div> 
                <input />        
                <span @click="handleClick">            
                    <slot>这里是插槽的默认值</slot>        
                </span>    
            </div>`</span>&#125;)
<span class="hljs-keyword">const</span> vm = app.mount(<span class="hljs-string">"#root"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有时候我们希望不同的slot渲染不同的内容，这个时候，具名插槽对我们就很有用了，就像这样</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> app= Vue.createApp(&#123;    
    <span class="hljs-attr">template</span>: <span class="hljs-string">`<layout>            
    // 一定通过template标签，不能将v-slot作用在h5标签上            
    <template v-slot:header>                
        <div>header</div>            
    </template>            
    <template v-slot:footer>                
        <div>footer</div>            
    </template>        
</layout>`</span>&#125;)
app.component(<span class="hljs-string">'layout'</span>,&#123;    
    <span class="hljs-attr">template</span>: <span class="hljs-string">`<div>        
                <slot name="header"></slot>        
                <div>content</div>        
                <slot name="footer"></slot>    
            </div>`</span>
&#125;)
<span class="hljs-keyword">const</span> vm = app.mount(<span class="hljs-string">"#root"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，我们也可以通过#简写成这样</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> app= Vue.createApp(&#123;    
    <span class="hljs-attr">template</span>: <span class="hljs-string">`<layout>            
            // 通过#替代v-slot            
            <template #header>                
                <div>header</div>            
            </template>            
            <template #footer>                
                <div>footer</div>            
            </template>        
        </layout>`</span>&#125;)
app.component(<span class="hljs-string">'layout'</span>,&#123;    
    <span class="hljs-attr">template</span>: <span class="hljs-string">`<div>        
                    <slot name="header"></slot>        
                <div>content</div>        
                <slot name="footer"></slot>    
            </div>`</span>&#125;)
<span class="hljs-keyword">const</span> vm = app.mount(<span class="hljs-string">"#root"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有时候，我们可能需要在子组件渲染数据，然后在父组件定义不同的标签，这个时候，我们会用到作用域标签</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> app= Vue.createApp(&#123;    
    <span class="hljs-attr">template</span>: <span class="hljs-string">`<mylist />        
    // 作用域插槽        
        <mylist v-slot="slotProps">            
            <span>&#123;&#123;slotProps.item&#125;&#125;</span>            
        </mylist>`</span>
&#125;)
app.component(<span class="hljs-string">'mylist'</span>,&#123;    
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span>&#123;        
        <span class="hljs-keyword">return</span> &#123;            
            <span class="hljs-attr">list</span>: [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>]        
        &#125;    
    &#125;,    
    <span class="hljs-attr">template</span>: <span class="hljs-string">`<div>            
                <slot v-for="item in list" :item="item"></slot>       
            </div>`</span>&#125;)
<span class="hljs-keyword">const</span> vm = app.mount(<span class="hljs-string">"#root"</span>)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            