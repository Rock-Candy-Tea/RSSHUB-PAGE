
---
title: '「站在上帝的角度」谈谈Element组件结构-Rate'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9854e883018c4f90ba301e0f15fa29fb~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 00:00:58 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9854e883018c4f90ba301e0f15fa29fb~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第6天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">前言👋</h2>
<ul>
<li>用户就是上帝，站在上帝的角度也就是站在使用者的角度去看待组件。</li>
<li>用过不少优秀的<code>UI</code>库，用的时候美滋滋，轮到自己搭组件库的时候往往会去参考别人的源码。</li>
<li>看完源码后恍然大悟 噢！原来可以这样写，但心里难免会有疑惑别人是怎么想出来这种解决思路的？🤳</li>
<li>这一系列文章主要是面向未理解或者有疑惑的同学所以讲的比较基础，就让我们站在用户的角度去思考结构，看看换一种思路去写代码是不是有变化？</li>
</ul>
<h2 data-id="heading-1">关于Rate组件⭐</h2>
<h3 data-id="heading-2">为什么我们会用到Rate</h3>
<h4 data-id="heading-3">作为用户👨‍💼</h4>
<ul>
<li>前面也说了很多次，用户更加注重的是视觉上的冲击主要以方便为主，试想要给一个产品或者美食评分你会选择手输入<code>90</code> <code>100</code>分还是希望有个东西可以点击选择，我想大部分都会选择第二种。</li>
<li>所以现在不管是移动端还是pc端，现在越来越多的评分按钮出现在我们的眼前，不仅是为了美观还有的是满足我们的<code>懒人心理</code></li>
</ul>
<h4 data-id="heading-4">作为组件库使用者👨‍💻</h4>
<ul>
<li>我们可以看到很多的组件库都有<code>Rate</code>，<code>Rate</code>翻译成中文是比率，等级的意思。</li>
<li>当我们将组件库的<code>Rate</code>组件放到我们的页面我们想要的效果是什么？
<ul>
<li>有亮丽的颜色对比</li>
<li>可以满足基本的选择需求</li>
<li>可以用百分比来展示所选的评分（比如：<code>半星</code> <code>小数点评分</code>）</li>
<li>可以在基本的需求上进行定制增加功能（比如:<code>颜色属性</code> <code>禁用</code> <code>是否添加文字</code> ）</li>
</ul>
</li>
<li>在某一个方面来说，<code>Rate</code>的出现也让我们在制作页面时给了用户除了选择下拉框，开关之外有其他的选择，说白了就是让页面更加鲜艳了不会那么单调。</li>
</ul>
<h2 data-id="heading-5">搭建组件⚒️</h2>
<blockquote>
<p>接下来可能用尽可能少的代码搭配<code>element</code>的源码进行结构说明，配合<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FElemeFE%2Felement%2Fblob%2Fdev%2Fpackages%2Frate%2Fsrc%2Fmain.vue" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ElemeFE/element/blob/dev/packages/rate/src/main.vue" ref="nofollow noopener noreferrer">element Rate</a>源码食用更加美味喔</p>
</blockquote>
<h3 data-id="heading-6">基本架子🔨</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9854e883018c4f90ba301e0f15fa29fb~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>要设计一个上图这种的<code>Rate</code>不难，我们会需要五个容器假设为空，当我们鼠标经过后会填充，当我们鼠标选择后他会停留最后一次所有选择填充的<code>容器数</code>，当我们鼠标离开后他会回到最初点击前的状态。</li>
<li>总结起来总共也只有<code>4</code>个要点
<ul>
<li>准备一个外部的五个初始元素</li>
<li>准备一个鼠标触摸事件、鼠标点击事件和一个鼠标离开容器的事件</li>
<li>各种事件呈现的效果顺带加上亿点点的过渡效果</li>
<li>双向绑定组件外的值和子组件的值</li>
</ul>
</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e52bd88cf074be18c3f561560c319a8~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable"><template>
  <div class="zl-rate">
    <span
      v-for="(item, key) in max"
      :key="key"
      class="zl-rate__item"
    >
      <i class="zl-icon-aixin_shixin"></i>
    </span>
  </div>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>以上就是<code>element</code>最简单的<code>rate</code>结构，可以看到子组件接受一个<code>max</code>来控制图标个数，再将<code>span</code>遍历即可，这里我用v-model传了一个<code>value</code>,具体怎么使用我会在下面解释，这里我个人的组件用了个人的爱心图标~❤️具体样式可以看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FElemeFE%2Felement%2Fblob%2Fdev%2Fpackages%2Ftheme-chalk%2Fsrc%2Frate.scss" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ElemeFE/element/blob/dev/packages/theme-chalk/src/rate.scss" ref="nofollow noopener noreferrer">element 样式</a></li>
<li>当然这只是一个架子我们还需要加上触摸事件和点击事件让他填充起来</li>
</ul>
<h3 data-id="heading-7">设置事件🧨</h3>
<ul>
<li>填充其实就是改变了颜色，首先我们准备两个颜色一个代表空一个代表填充</li>
<li>因为我们的爱心是通过遍历而形成的我们可以鼠标移动到该元素就可以用<code>currentValue</code>记录下来该元素的<code>item</code>，当<code>currentValue</code>大于等于<code>item</code>时那么就说明我们已经经过了这个爱心所以他应该是填充的颜色，通过这个思路可以动态切换我们的颜色样式</li>
<li>在设置一个鼠标移出事件当我们鼠标移出爱心时就清空所有回到最初的状态，这里清空的时候让<code>currentValue</code>回归到外部传进来的<code>value</code>值，而这个<code>value</code>值是怎么来的呢相信看过我之前两篇文章的同学已经很熟悉就是<code>v-model</code>的语法糖自动生成的。</li>
</ul>
<pre><code class="copyable">template 
    ...
    <span
      v-for="(item, key) in max"
      :key="key"
      class="zl-rate__item"
      @mousemove="setCurrentValue(item, $event)"
      @mouseleave="resetCurrentValue"
    >
      <i 
        class="zl-icon-aixin_shixin "
        :class="[&#123; 'hover': hoverIndex === item &#125;]"
        :style="getIconStyle(item)"
      ></i>
    </span>
    ...
    
script
    ...
      props:&#123;
        value: &#123;
          type: Number,
          default: 0
        &#125;,
        max: &#123;
          type: Number,
          default: 5
        &#125;,
      &#125;,
      data()&#123;
        return&#123;
          currentValue:0,
          hoverIndex: -1,
          voidColor:'#C6D1DE',
          activeColor:'red'
        &#125;;
      &#125;,
      methods:&#123;
        setCurrentValue(value) &#123;
              this.currentValue = value;
              this.hoverIndex = value;
        &#125;,
        resetCurrentValue() &#123;
            //清空颜色
          this.currentValue = this.value;
          this.hoverIndex = -1;
        &#125;,
        getIconStyle(item) &#123;
          const voidColor = this.voidColor;//默认颜色（即空的颜色）
          return &#123;
            //是否小于选中的值，是则填充颜色否则则为默认
            color: item <= this.currentValue ? this.activeColor : voidColor
          &#125;;
        &#125;
      &#125;
    ...

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0202932edc9b4666ab800f84a1ecdd50~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">双向绑定🎶</h3>
<ul>
<li>现在我们的爱心可以随着鼠标移动和移出来控制样式了</li>
<li>但是单单只是颜色变换可不行，我们需要记录下来点击后的数值，这时候就需要用到外面的<code>v-model</code>了</li>
<li>在父组件我们用<code>v-model</code>传入了一个值， 而<code>v-model</code>的语法糖会把这个值当成<code>props</code>的<code>value</code>传到子组件，子组件只要通过<code>$emit</code>时间改变外部的<code>input</code>事件就可以啦。</li>
</ul>
<pre><code class="copyable">···
    <span
          v-for="(item, key) in max"
          :key="key"
          class="zl-rate__item"
          @mousemove="setCurrentValue(item, $event)"
          @mouseleave="resetCurrentValue"
          @click="selectValue(item)"
        >
          <i 
            class="zl-icon-aixin_shixin "
            :class="[&#123; 'hover': hoverIndex === item &#125;]"
            :style="getIconStyle(item)"
          ></i>
    </span>
···

···
    selectValue(value) &#123;
        this.$emit('input', value);
    &#125;,
···
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在这里我们增加一个鼠标点击事件，这样我们点击爱心时就会记录当前的value传到父组件,父组件就可以根据这个值来做一些逻辑，内部的子组件因为鼠标移出事件<strong>使子组件的<code>currentValue</code></strong> 自动接收了外部的<code>value</code>让爱心在视觉上是填满了的。</li>
<li>这样一来我们的一个最简单的<code>rate</code>就做好了。</li>
</ul>
<h3 data-id="heading-9">更多需求🧮</h3>
<ul>
<li>一个最简单的架子搭好了接下来就可以定制我们的组件了。</li>
<li>比如说禁用啊，加文字啊，相信大家也已经很熟悉了，无非就是通过插槽获取通过<code>props</code>实现动态样式切换即可。</li>
<li>当然<code>element</code>的<code>Rate</code>也做了半星等操作,这次的组件结构就分享到这里啦，更多的实现可以参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FElemeFE%2Felement%2Fblob%2Fdev%2Fpackages%2Frate%2Fsrc%2Fmain.vue" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ElemeFE/element/blob/dev/packages/rate/src/main.vue" ref="nofollow noopener noreferrer">传送门</a>进行学习~</li>
</ul>
<h2 data-id="heading-10">写在最后👋</h2>
<ul>
<li>总的来说<code>Rate</code>组件相对于其他复杂组件比较简单，难点在于如何控制半星等样式操作。</li>
<li>对于组件库的搭建我也在慢慢的摸索，讲的都是我自己得出来的分享所以说可能对于大佬来说会比较基础，但我相信我的不断输出可以帮助到一些有疑惑的同学。</li>
<li>如果您觉得这篇文章有帮助到您的的话不妨<strong>🍉关注+点赞+收藏+评论+转发🍉</strong>支持一下哟~~😛</li>
</ul>
<h2 data-id="heading-11">往期精彩🌅</h2>
<p><a href="https://juejin.cn/post/6991267694678900772" target="_blank" title="https://juejin.cn/post/6991267694678900772">如何优雅的使用Vuepress编写组件示例（上）👈</a></p>
<p><a href="https://juejin.cn/post/6991646499775971359" target="_blank" title="https://juejin.cn/post/6991646499775971359">如何优雅的使用Vuepress编写组件示例（下）👈</a></p>
<p><a href="https://juejin.cn/post/6992770501940609055" target="_blank" title="https://juejin.cn/post/6992770501940609055">「站在上帝的角度」谈谈Element组件结构-Switch</a></p>
<p><a href="https://juejin.cn/post/6992385934255734798" target="_blank" title="https://juejin.cn/post/6992385934255734798">「站在上帝的角度」谈谈Element组件结构-Radio</a></p></div>  
</div>
            