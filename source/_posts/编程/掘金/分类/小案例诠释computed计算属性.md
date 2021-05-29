
---
title: '小案例诠释computed计算属性'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95a78a05268d437886e6a5566f7dea4e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 28 May 2021 06:40:22 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95a78a05268d437886e6a5566f7dea4e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这个小案例的需求是：</p>
<ol>
<li>
<p>切换到全部就只显示全部的内容</p>
</li>
<li>
<p>切换到未结算就只显示未结算的内容</p>
</li>
<li>
<p>切换到结算就只显示结算的内容</p>
</li>
<li>
<p>切换到失效就只显示失效的内容</p>
</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95a78a05268d437886e6a5566f7dea4e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-0">一、页面布局</h4>
<pre><code class="copyable"><template>
  <div class="home">
    <el-tabs v-model="status" @tab-click="handleClick">
      <el-tab-pane label="全部" name="0"></el-tab-pane>
      <el-tab-pane label="未结算" name="1"></el-tab-pane>
      <el-tab-pane label="已结算" name="2"></el-tab-pane>
      <el-tab-pane label="失效" name="3"></el-tab-pane>
    </el-tabs>
    <div class="content" v-for="item in tabContent" :key="item.id">
      <p>&#123;&#123;item.name&#125;&#125;</p>
      <p>&#123;&#123;fillStatus(item.status)&#125;&#125;</p>
    </div>
  </div>
</template>
<style lang="scss">
  .home &#123;
    max-width: 300px;
    margin: 100px auto;
    .content &#123;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 10px;
      margin-bottom: 15px;
      border-bottom: 1px solid #e4e7ed;
    &#125;
  &#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>数据data，其中listData模拟当时后端的数据</p>
<pre><code class="copyable">data () &#123;
    return &#123;
      listData: [&#123;
        id: 1,
        name: '产品1',
        status: '2'
      &#125;, &#123;
        id: 2,
        name: '产品2',
        status: '1'
      &#125;, &#123;
        id: 3,
        name: '产品3',
        status: '3'
      &#125;, &#123;
        id: 4,
        name: '产品4',
        status: '3'
      &#125;],
      status: '0', // 未结算1；已结算2；失效3
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时的页面展示效果是这样的</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26f12f0ef99840e1a3ade8b25a6d1009~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-1">二、把status 未结算1，已结算2，失效3，相对应数字转换文字</h4>
<pre><code class="copyable">methods: &#123;
    fillStatus (status) &#123;
      if (status === '1') return '未结算'
      if (status === '2') return '已结算'
      if (status === '3') return '失效'
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相应的在html里传参</p>
<pre><code class="copyable"><div class="content" v-for="item in listData" :key="item.id">
  <p>&#123;&#123;item.name&#125;&#125;</p>
  <p>&#123;&#123;fillStatus(item.status)&#125;&#125;</p>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时页面效果</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83d8e473a6ee46dbae3713d0a77449a2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">三、1. 切换到全部就只显示全部的内容；2. 切换到未结算就只显示未结算的内容；3. 切换到结算就只显示结算的内容；4. 切换到失效就只显示失效的内容（本文章核心）</h4>
<p><strong>computed计算属性</strong>，可以在页面上进行双向数据绑定展示出结果或者用作其他处理，<strong>依赖数据data的变化而变化</strong>，<strong>有缓存</strong>，即<strong>只在需要时更新</strong>。</p>
<p>watch数据监听，监听数据data的变化，起到 观察员 的作用，无缓存。</p>
<p>在这个小案例中 computed得到一个很好的诠释。</p>
<pre><code class="copyable">computed: &#123;
    tabContent () &#123;
      return this.listData.filter(item => &#123;
        if (this.status === '0') return item
        return item.status === this.status
      &#125;)
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后在这里贴上完整的代码：</p>
<pre><code class="copyable"><template>
  <div class="home">
    <el-tabs v-model="status" @tab-click="handleClick">
      <el-tab-pane label="全部" name="0"></el-tab-pane>
      <el-tab-pane label="未结算" name="1"></el-tab-pane>
      <el-tab-pane label="已结算" name="2"></el-tab-pane>
      <el-tab-pane label="失效" name="3"></el-tab-pane>
    </el-tabs>
    <div class="content" v-for="item in tabContent" :key="item.id">
      <p>&#123;&#123;item.name&#125;&#125;</p>
      <p>&#123;&#123;fillStatus(item.status)&#125;&#125;</p>
    </div>
  </div>
</template>

<script>
export default &#123;
  name: 'Home',
  data () &#123;
    return &#123;
      listData: [&#123;
        id: 1,
        name: '产品1',
        status: '2'
      &#125;, &#123;
        id: 2,
        name: '产品2',
        status: '1'
      &#125;, &#123;
        id: 3,
        name: '产品3',
        status: '3'
      &#125;, &#123;
        id: 4,
        name: '产品4',
        status: '3'
      &#125;],
      status: '0' // 未结算1；已结算2；失效3
    &#125;
  &#125;,
  computed: &#123;
    tabContent () &#123;
      return this.listData.filter(item => &#123;
        if (this.status === '0') return item
        return item.status === this.status
      &#125;)
    &#125;
  &#125;,
  methods: &#123;
    fillStatus (status) &#123;
      if (status === '1') return '未结算'
      if (status === '2') return '已结算'
      if (status === '3') return '失效'
    &#125;,
    // tab 被选中时触发
    handleClick (val) &#123;
      this.status = val.index
      console.log(val.index)
    &#125;
  &#125;
&#125;
</script>
<style lang="scss">
  .home &#123;
    max-width: 300px;
    margin: 100px auto;
    .content &#123;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 10px;
      margin-bottom: 15px;
      border-bottom: 1px solid #e4e7ed;
      &:last-child &#123;
        border-bottom: none;
      &#125;
    &#125;
  &#125;
</style>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>进入前端这一行，是大学在图书馆的一本小程序的书籍懵懵懂懂的照着书籍的案例敲出代码，初入社会，一切从0开始，先是基础课再到实操课，以及中间持续翻看文档。但<strong>无论是何种学习方式，离不开官方文档，离不开自己独立的思想，以及最重要的实操</strong>。我觉得程序员这个行业，最重要的就是实操，bug写多了，坑踩多了，经验就多了，能力也就上去了。
我想，我的压力主要是因为自己的经验不足，比如一个看上去较小的bug，感觉20多分钟就能搞定，但最后弄了3个多小时。</p>
<p>今天的你，放下浮躁，放下慵懒，放下三分钟热度，放空经不住诱惑的大脑，放开容易被任何事物吸引的眼睛，静下心来，写bug了吗？</p>
<p>哈哈哈，今天又是美好快乐的一天。</p></div>  
</div>
            