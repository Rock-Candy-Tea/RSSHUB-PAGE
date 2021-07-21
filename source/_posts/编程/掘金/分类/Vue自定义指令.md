
---
title: 'Vue自定义指令'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6413'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 22:54:40 GMT
thumbnail: 'https://picsum.photos/400/300?random=6413'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Vue允许注册自定义指令,当对普通DOM元素进行底层操作这个时候就会用到自定义指令.</h2>
<h3 data-id="heading-1">初识 input自动获得焦点</h3>
<h4 data-id="heading-2">1.注册一个全局的指令</h4>
<pre><code class="copyable"><input type="text" v-model="num" v-focus>
Vue.directive('focus', &#123;
    // 当被绑定的元素插入到DOM中时
    inserted: function (el) &#123;
        // 聚焦元素
        el.focus();
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">2.注册一个局部组件</h4>
<pre><code class="copyable"> // 注册局部组件
<input type="text" v-model="num" v-focus>
directives: &#123;
    focus: &#123;
        // 被绑定元素插入父节点时调用(仅保证父节点存在,但不一定已被插入文档中)
        inserted: function (el) &#123;
            console.log(el, 'inserted')
            //设置获取焦点
            el.focus();
        &#125;,
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">钩子函数</h3>
<pre><code class="copyable">// html页面
<input type="text" v-model="num" v-focus:foo.x="message" v-if="num<20">
// Vue数据
data: &#123;
    num: 1,
    message: 'hello!',
&#125;
// 注册局部组件
directives: &#123;
    focus: &#123;
        // 只调用一次,指令第一次绑定到元素时调用,在这里可以进行一次性的初始化设置.
        bind: function (el, vnode) &#123;
            console.log(el, 'bind');
        &#125;,
        // 被绑定元素插入父节点时调用(仅保证父节点存在,但不一定已被插入文档中)
        inserted: function (el) &#123;
            console.log(el, 'inserted')
            //设置获取焦点
            el.focus();
        &#125;,
        // 所有组件的VNode更新时调用,但是可能发生在其子VNode更新之前,指令的值可能发生了改变,也可能没有,但是你可以通过比较更新前后的值来忽略不必要的模板更新
        update: function (el, binding, vnode, oldVnode) &#123;
            console.log('update start');
            console.log(binding, 'binding', new Date().toLocaleString());
            // <input type="text" v-model="num" v-focus:foo.x="message" v-if="num<20">
            // data: &#123;
            //     num: 1,
            //     message: 'hello!'
            // &#125;,
            //binding:一个对象,包含以下property
            //      name:指令名 不包括v-前缀 focus
            //      value:指令的绑定值  hello!
            //      oldValue:指令绑定的前一个值,仅在update和componentUpdate钩子中可用,无论值是否改变都可用
            //      expression字符串形式的指令表达式,例如 v-focus:foo.x="message"中,表达式为 message
            //      arg:传给指令的参数,可选,例如v-focus:foo.x="message" 中,参数为 foo
            //      modifiers:一个包含修饰符的对象,例如:v-focus:foo.x="message"中,修饰符对象为&#123;x:true&#125;

        &#125;,
        // 指令所有组件的VNode及其子 VNode全部更新后调用
        componentUpdated: function (el) &#123;
            console.log('update end');
            console.log(el, 'componentUpdated');
        &#125;,
        // 只调用一次,指令与元素解绑时调用 由于设置v-if<20 所以当输入大于19的数字就会执行这个钩子函数
        unbind: function (el) &#123;
            console.log(el, 'unbind');
        &#125;
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">动态指令参数</h3>
<pre><code class="copyable">// html
<div v-fixed:[position]="px" class="odiv"></div>
// vue数据
data: &#123;
    position: 'right',
    px: 300
&#125;,
// vue自定义函数部分
// 动态指令参数 设置固定定位 距右300px
fixed: &#123;
    bind: function (el, binding, vnode) &#123;
        el.style.position = 'fixed'
        el.style[binding.arg] = binding.value + 'px'
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            