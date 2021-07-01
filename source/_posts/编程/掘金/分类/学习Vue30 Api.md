
---
title: '学习Vue3.0 Api'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7592'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 02:01:20 GMT
thumbnail: 'https://picsum.photos/400/300?random=7592'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>愿舒适的晚风和星空 带走一切坏情绪。</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;&#123; msg &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"count++;num--"</span>></span>count is: &#123;&#123; count &#125;&#125;&#123;&#123;num&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"addNum"</span>></span>Edit <span class="hljs-tag"><<span class="hljs-name">code</span>></span>components/HelloWorld.vue<span class="hljs-tag"></<span class="hljs-name">code</span>></span> to test hot module replacement.<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(item,index) in numCopy.stus"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"index"</span>></span>&#123;&#123;item.key&#125;&#125;&#123;&#123;numCopy&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; ref, reactive &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'HelloWorld'</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">msg</span>: <span class="hljs-built_in">String</span>
  &#125;,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
    &#125;
  &#125;,
  <span class="hljs-comment">//   组合api入口函数，是在beforecreate钩子之前完成的   无法使用 data和 methods</span>
  <span class="hljs-comment">/**
   * 
   */</span>
  setup () &#123;
    <span class="hljs-comment">//reactive   ref   同理使用proxy</span>
    <span class="hljs-comment">/**
        function ref (obj) &#123;
        return reactive(&#123; value: obj &#125;)
        &#125;
        function reactive (obj) &#123;
        if (typeof obj === 'object') &#123;
            if (obj instanceof Array) &#123;
            //如果是数组，取出数组中的每一个元素
            //判断其是否是一个对象，是否需要包装成proxy
            obj.forEach((item, index) => &#123;
                if (typeof item === 'object') &#123;
                obj[index] = reactive(item)
                &#125;
            &#125;)
            &#125; else &#123;
            //如果是对象，取出对象中的每一个value
            //判断其是否是一个对象，是否需要包装成proxy
            for (let key in obj) &#123;
                let item = obj[key];
                if (typeof item === 'object') &#123;
                obj[key] = reactive(item)
                &#125;
            &#125;
            &#125;
        &#125;
        &#125;
    */</span>

    <span class="hljs-comment">//手写一个shallowRef     </span>
    <span class="hljs-comment">/**
        function shallowRef(obj)&#123;
            return shallowReactive(&#123;value:obj&#125;);
        &#125;
        
        function shallowReactive(obj)&#123;
            return newProxy(obj,&#123;
                get(obj,key)&#123;
                    return obj[key]
                &#125;,
                set(obj,key,value)&#123;
                    obj[key=value];
                    console.log('页面更新')
                    return true;//这个必须
                &#125;
            &#125;)
        &#125;
     */</span>
    <span class="hljs-comment">//vue3.0响应式数据的本质</span>
    <span class="hljs-comment">/**
        proxy  //= 
        set方法必须通过返回值告诉proxy此次操作是否成功 

        let obj=&#123;name:'ll',age:'18'&#125;
        let state=new proxy(obj,&#123;
            get(obj,key)&#123;             //监听外界有没有获取值
                console.log(obj,key);
                return obj[key]
            &#125;,
            set(obj,key,value)&#123;
                console.log(obj,key,value)
                obj[key]=value;
                console.log('更新ui)

                //需要添加
                return true
            &#125;
        &#125;)
        console.log(state.name)
        state.name="???"
     */</span>


    <span class="hljs-comment">/**
       readonly 可定义只读数据   递归只读   shallowReadonly   第一层只读，非递归只读    isReadonly判断是否只读？callback  bool
       与const  区别是  const为变量赋值保护，readonly属性赋值保护
     */</span>
    <span class="hljs-comment">/**
        组合api也可以加入生命周期
        onMounted  onCreated 。。。
        onMounted（（）=》&#123;
            。。。
        &#125;）
     */</span>
    <span class="hljs-comment">//ref函数和reactive函数都可监听所有数据类型（递归监听）</span>
    <span class="hljs-comment">//默认情况下递归监听是好的，可以让数据变化是是被监听到，但是也带来了性能消耗问题；</span>
    <span class="hljs-comment">// 内部函数为同步，不可异步</span>
    <span class="hljs-comment">/**
     *  2.非递归监听
        shallowRef / shallowReactive

        3.如何触发非递归监听属性更新界面?
        - 如果是shallowRef类型数据, 可以通过triggerRef来触发
        - 注意点: 如果是通过shallowRef创建数据,      ！！！
        -- 那么Vue监听的是.value的变化, 并不是第一层的变化
        4.应用场景
        一般情况下我们使用 ref和reactive即可
        只有在需要监听的数据量比较大的时候, 我们才使用shallowRef/shallowReactive
     */</span>
    <span class="hljs-comment">//shallow类型的数据，只会监听最外层的数据的变化，才会引起视图层的变化</span>
    <span class="hljs-comment">//对于 shallowRef 过的 ref 对象，我们还可以 triggerRef 去触发 ref 的变化监听来实现界面的改变</span>
    <span class="hljs-comment">//----在 shallowReactive 中，并没有提供 trigger 方案来主动唤醒监测变化。</span>
    <span class="hljs-comment">/**
     * 本质上，shallowRef 是特殊的 shallowReactive，而 ref 是特殊的 reactive。
     */</span>
    <span class="hljs-keyword">let</span> &#123; num, addNum, numCopy &#125; = numTagger();<span class="hljs-comment">//提出</span>
    <span class="hljs-keyword">let</span> state2 = reactive(&#123;<span class="hljs-comment">//参数必须为对象</span>
      <span class="hljs-attr">stu</span>: [
        &#123;
          <span class="hljs-attr">id</span>: <span class="hljs-string">'1'</span>,
          <span class="hljs-attr">name</span>: <span class="hljs-string">'aa'</span>,
          <span class="hljs-attr">age</span>: <span class="hljs-string">'23'</span>
        &#125;,
        &#123;
          <span class="hljs-attr">id</span>: <span class="hljs-string">'2'</span>,
          <span class="hljs-attr">name</span>: <span class="hljs-string">'bb'</span>,
          <span class="hljs-attr">age</span>: <span class="hljs-string">'34'</span>
        &#125;,
        &#123;
          <span class="hljs-attr">id</span>: <span class="hljs-string">'3'</span>,
          <span class="hljs-attr">name</span>: <span class="hljs-string">'cc'</span>,
          <span class="hljs-attr">age</span>: <span class="hljs-string">'45'</span>
        &#125;,
      ]
    &#125;)
    <span class="hljs-comment">/**
     * 当我们修改了ref、reactive中的数据时，又不需要其更新视图，可以使用toRaw方法（追踪到原始数据 ）
     * let objCopy=toRaw（obj）
     * 修改objCopy的值
     * 
     * 
     * markRaw（）永远不要追踪！之后追踪无效
     * 
     * 
     * ref（obj。name）obj中的name变为响应式，修改name对之前的obj。name没有影响。
     * toRef（obj，‘name’）  会影响到obj中的name，但是如果响应式是通过toRef创建的，修改不会触发ui更新
     * ==》应用场景。。想让响应式数据和之前的数据关联起来，并且更新响应式数据后不想更新ui就使用toRef（）
     * ==》多重toRefs（）obj对象中多个属性变化使用。
     * 
     * 
     * customRef   自定义一个ref   适用于想把异步数据，假装成同步
      function myRef(value)&#123;
          return customRef((track,trigger)=>&#123;
              、、网络请求可以放到这里
              return &#123;
                  get()&#123;
                    不能在这里发送网络请求：
                    渲染界面=》调用get=》发送网络请求=》保存数据=》更新页面=》调用get
                      track();//告诉Vue这个数据是需要追踪变化的
                      return value
                  &#125;,
                  set(newValue)&#123;
                      value = newValue；
                      trigger();//告诉ui数据发生了变化
                  &#125;
              &#125;
          &#125;)
      &#125;
     */</span>
    <span class="hljs-keyword">return</span> &#123; num, addNum, numCopy, state2 &#125;;<span class="hljs-comment">//返回暴漏</span>
  &#125;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">numTagger</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> num = ref(<span class="hljs-number">0</span>);<span class="hljs-comment">//定义并未暴漏</span>
  <span class="hljs-keyword">let</span> numCopy = reactive(&#123;
    <span class="hljs-attr">stus</span>: [
      &#123;
        <span class="hljs-attr">key</span>: <span class="hljs-number">0</span>
      &#125;,
      &#123;
        <span class="hljs-attr">key</span>: <span class="hljs-number">1</span>
      &#125;,
      &#123;
        <span class="hljs-attr">key</span>: <span class="hljs-number">2</span>
      &#125;,
      &#123;
        <span class="hljs-attr">key</span>: <span class="hljs-number">3</span>
      &#125;
    ]
  &#125;)
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addNum</span> (<span class="hljs-params"></span>) </span>&#123;<span class="hljs-comment">//直接定义方法</span>
    <span class="hljs-built_in">console</span>.log(num, numCopy)
  &#125;
  <span class="hljs-keyword">return</span> &#123; num, addNum, numCopy &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>此时学习应不是太晚</strong></p>
<p>看大佬视频学习Vue3.0 附一个链接 <a href="https://www.bilibili.com/video/BV14k4y117LL?p=1" target="_blank" rel="nofollow noopener noreferrer">www.bilibili.com/video/BV14k…</a>；自带倍速，句句重点，幽默诙谐。</p>
<p><strong>over</strong> 🧐</p></div>  
</div>
            