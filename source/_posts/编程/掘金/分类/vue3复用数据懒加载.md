
---
title: 'vue3复用数据懒加载'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/918d1cc5e05a4cdfa6c3bba3651a3ee9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 18:18:05 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/918d1cc5e05a4cdfa6c3bba3651a3ee9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1. 借用插件</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fvueuse.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://vueuse.org/" ref="nofollow noopener noreferrer">@vueuse/core</a></p>
<p>插件的底层原理用到了h5中的# IntersectionObserver()</p>
<p>详情请看：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FIntersectionObserver%2FIntersectionObserver" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserver/IntersectionObserver" ref="nofollow noopener noreferrer">IntersectionObserver</a></p>
<pre><code class="copyable">npm i @vueuse/core
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">2. 引用插件</h2>
<pre><code class="copyable">import &#123; useIntersectionObserver &#125; from '@vueuse/core'
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">3.使用</h2>
<pre><code class="copyable"><template>
    <div ref="target"></div>
</template>

<script>
    export default&#123;
        setup()&#123;
           const target = ref(null) // 把目标引用
           const &#123; stop &#125; = useIntersectionObserver(
              target, // target 是vue的对象引用。是观察的目标
              // isIntersecting 是否进入可视区域，true是进入 false是移出
              // observerElement 被观察的dom
              ([&#123; isIntersecting &#125;], observerElement) => &#123;
                // 在此处可根据isIntersecting来判断（判断dom元素是否在可是区域内），然后做业务
                if (isIntersecting) &#123;
                  // 1. 停止观察
                  stop()
                  // 2. 发一次请求
                  //发送ajax
                &#125;
              &#125;
            )

            return &#123; list, target &#125;
        &#125;
    &#125;
</script>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">4. 对数据懒加载进行封装</h2>
<p>这里将此文件放入<code>compositions/index.js</code>中</p>
<pre><code class="copyable">import &#123; useIntersectionObserver &#125; from '@vueuse/core'
import &#123; ref &#125; from 'vue'

/**
 * 功能：数据的懒加载
 * @param &#123;*&#125; fn 当目标可见时，需要调用一次函数
 * @returns target：要观察的目标元素（dom元素）
 */
export function useLazyData (fn) &#123;
  const target = ref(null) // 把目标引用
  const &#123; stop &#125; = useIntersectionObserver(
    target, // target 是vue的对象引用。是观察的目标
    // isIntersecting 是否进入可视区域，true是进入 false是移出
    // observerElement 被观察的dom
    ([&#123; isIntersecting &#125;], observerElement) => &#123;
      // 在此处可根据isIntersecting来判断，然后做业务
      if (isIntersecting) &#123;
        // 1. 停止观察
        stop()
        // 2. 发一次请求
        fn()
      &#125;
    &#125;
  )
  return target
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">5. 使用封装好的数据懒加载</h2>
<pre><code class="copyable"><template>
    <div ref="target"></div>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">import &#123; useLazyData &#125; from '@/compositions/index.js'
<script>
setup () &#123;
    const goods = ref([])
    const fn = () => &#123;
      //业务代码（请求数据）
    &#125;
    const target = useLazyData(fn)

    return &#123; goods, target &#125;
  &#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">6. 效果图</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/918d1cc5e05a4cdfa6c3bba3651a3ee9~tplv-k3u1fbpfcp-watermark.image" alt="小兔仙数据懒加载效果图.gif" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            