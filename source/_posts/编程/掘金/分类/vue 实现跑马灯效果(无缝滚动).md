
---
title: 'vue 实现跑马灯效果(无缝滚动)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9814'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 02:46:03 GMT
thumbnail: 'https://picsum.photos/400/300?random=9814'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>项目上用到一个跑马灯的组件（支持文字、图片的无缝滚动），没有找到开源的合适的组件，索性自己实现一个。</p>
<h3 data-id="heading-0">实现原理：</h3>
<p>用到HTML element 的两个属性：scrollLeft和scrollWidth。</p>
<ol>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FElement%2FscrollLeft" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/Element/scrollLeft" ref="nofollow noopener noreferrer"> scrollLeft </a>:读取或设置元素滚动条到元素左边的距离。</p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2Felement%2FscrollWidth" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/element/scrollWidth" ref="nofollow noopener noreferrer">scrollWidth</a>:只读属性，是对元素内容宽度的一种度量，包括由于overflow溢出而在屏幕上不可见的内容</p>
</li>
</ol>
<p>简单来说，就是获取滚动元素的scrollWidth，然后不断的设置scrollLeft的值就可以了。</p>
<h3 data-id="heading-1">show you my code:</h3>
<p>👇下面是跑马灯组件：</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div class="show-area" :style="&#123; width: `$&#123;width&#125;px`, height: `$&#123;height&#125;px` &#125;">
    <div class="scroll-area">
      <!-- 设置margin，使内容 有从无到有的出现效果 -->
      <div class="slot-container" :style="&#123; margin: `0 $&#123;width&#125;px` &#125;">
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue, &#123; PropType &#125; from 'vue'

export default Vue.extend(&#123;
  props: &#123;
    // 自定义跑马灯宽度
    width: &#123;
      type: Number,
      default() &#123;
        return 400
      &#125;
    &#125;,
    // 自定义跑马灯高度
    height: &#123;
      type: Number,
      default: 50
    &#125;
  &#125;,
  data() &#123;
    return &#123;&#125;
  &#125;,
  mounted() &#123;
    // 在mounted阶段，才可以获取真实DOM节点
    const showArea: any = document.querySelector('.show-area')
    //从左到右滚动，首先把滚动条置到元素的最右边
    showArea.scrollLeft = showArea.scrollWidth
    function f() &#123;
      //如果滚动条到了元素的最左边，那么把它再初始化到最右边
      if (showArea.scrollLeft < 3) &#123;
        showArea.scrollLeft = showArea.scrollWidth
      &#125; else &#123;
        //每次滚动条向左移动2，改变speed可以调整滚动速度
        const speed = 2
        showArea.scrollLeft -= speed
      &#125;
      //使用requestAnimationFrame，优化滚动效果
      //requestAnimationFrame使得滚动和机器帧率同步
      requestAnimationFrame(f)
    &#125;
    requestAnimationFrame(f)
  &#125;
&#125;)
</script>

<style lang="scss" scoped>
.show-area &#123;
  // height: 50px;
  display: inline-block;
  white-space: nowrap;
  overflow: hidden;
  .scroll-area &#123;
    display: inline-block;
    .slot-container &#123;
      display: inline-block;
    &#125;
  &#125;
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>👇下面是一个demo：</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div class="carousel-c">
    <Carousel>
      <div v-for="item in items" :key="item">
        &#123;&#123; item &#125;&#125;
      </div>
    </Carousel>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import Carousel from '@components/common/carousel/carousel'

export default Vue.extend(&#123;
  components: &#123;
    Carousel
  &#125;,
  data() &#123;
    return &#123;
      items: ['文字1  ', '文字2  ', '文字3  ', '文字4  ', '文字5  ', '文字6  ']
    &#125;
  &#125;
&#125;)
</script>

<style scoped lang="scss"></style>

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            