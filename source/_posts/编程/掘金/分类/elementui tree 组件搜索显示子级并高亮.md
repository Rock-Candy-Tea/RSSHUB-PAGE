
---
title: 'elementui tree 组件搜索显示子级并高亮'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e82764836c547fc88b12705c89a03f0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 23:32:50 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e82764836c547fc88b12705c89a03f0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">功能介绍</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e82764836c547fc88b12705c89a03f0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>本节要优化的 el-Tree 组件具有以下功能：</p>
<ul>
<li>搜索之后显示所有的子级</li>
<li>节点匹配到关键字 高亮展示</li>
</ul>
<h4 data-id="heading-1">实现思路</h4>
<ul>
<li>通过自定义filter-node-method 去改变搜索的逻辑</li>
<li>高亮通过加入class类名显示</li>
</ul>
<h2 data-id="heading-2">Dom部分</h2>
<pre><code class="copyable"><el-tree
  ref="tree"
  :data="data"
  :props="props"
  :filter-node-method="filterNodeMethod"
  :highlight-current="true"
  node-key="value"
  :current-node-key="currentNodeKey"
  @node-click="handleNodeClick"
>
  <template #default="scope">
    <div
      :class="
        keyword === ''
          ? ''
          : scope.data.label.indexOf(keyword) !== -1
            ? 'has-key-word-style'
            : ''
      "
    >
      &#123;&#123; scope.data.label &#125;&#125;
    </div>
  </template>
</el-tree>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">js部分</h2>
<pre><code class="copyable">// 注意node参数 为所有节点
// 返回值为每个节点的visable属性值 决定是否展示
filterNodeMethod (value, data, node) &#123;
  if (!value) &#123;
    return true
  &#125;
  return this.getHasKeyword(value, node)
&#125;,

// 递归查找是否还有父节点

getHasKeyword (value, node) &#123;
  if (node.data instanceof Array) &#123;
    node.data = node.data.length > 0 ? node.data[0] : &#123;&#125;
  &#125;
  if (node.data.label && node.data.label.indexOf(value) !== -1) &#123;
    return true
  &#125; else &#123;
    return node.parent && this.getHasKeyword(value, node.parent)
  &#125;
&#125;



<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">完整代码</h2>
<pre><code class="copyable"><template>
  <div class="organization-tree">
    <span class="tree-title">&#123;&#123; title &#125;&#125;</span>
    <div class="tree-list">
      <div class="tree-filter">
        <el-input v-model="keyword" :placeholder="placeholder" @input="handleInput" />
        <el-button v-if="isCreate" icon="el-icon-plus" />
      </div>
      <div class="tree-all" :class="!activeNode ? 'tree-all-iscurrent' : ''" @click="clickAll">
        全部
      </div>
      <div class="tree-content">
        <el-tree
          ref="tree"
          :data="data"
          :props="props"
          :filter-node-method="filterNodeMethod"
          :highlight-current="true"
          node-key="value"
          :current-node-key="currentNodeKey"
          @node-click="handleNodeClick"
        >
          <template #default="scope">
            <div
              :class="
                keyword === ''
                  ? ''
                  : scope.data.label.indexOf(keyword) !== -1
                    ? 'has-key-word-style'
                    : ''
              "
            >
              &#123;&#123; scope.data.label &#125;&#125;
            </div>
          </template>
        </el-tree>
      </div>
    </div>
  </div>
</template>

<script>
export default &#123;
  name: 'OrganizationTree',
  props: &#123;
    isCreate: &#123;
      type: Boolean,
      default: true
    &#125;,
    title: &#123;
      type: String,
      default: '组织树'
    &#125;,
    data: &#123;
      type: Array,
      default: () => []
    &#125;,
    props: &#123;
      type: Object,
      default: () => (&#123;&#125;)
    &#125;,
    placeholder: &#123;
      type: String,
      default: '请输入关键字'
    &#125;
  &#125;,
  data () &#123;
    return &#123;
      keyword: '',
      currentNodeKey: null,
      activeNode: null // 默认激活全部
    &#125;
  &#125;,
  methods: &#123;
    async handleInput (v) &#123;
      this.$refs.tree.filter(v)
    &#125;,
    clickAll () &#123;
      this.activeNode = null
      this.$nextTick(() => &#123;
        this.$refs.tree.setCurrentKey(null)
      &#125;)
      this.$emit('all-click')
    &#125;,
    handleNodeClick (data, node) &#123;
      if (this.activeNode === data.value) &#123;
        // 二次点击
        this.clickAll()
        return
      &#125;
      this.activeNode = data.value
      this.$emit('node-click', data, node)
    &#125;,
    filterNodeMethod (value, data, node) &#123;
      if (!value) &#123;
        return true
      &#125;
      return this.getHasKeyword(value, node)
    &#125;,
    getHasKeyword (value, node) &#123;
      if (node.data instanceof Array) &#123;
        node.data = node.data.length > 0 ? node.data[0] : &#123;&#125;
      &#125;
      if (node.data.label && node.data.label.indexOf(value) !== -1) &#123;
        return true
      &#125; else &#123;
        return node.parent && this.getHasKeyword(value, node.parent)
      &#125;
    &#125;
  &#125;
&#125;
</script>

<style lang="scss">
.organization-tree &#123;
  background: #ffffff;
  width: 264px;
  border-radius: 2px;
  height: 100%;
  .tree-title &#123;
    display: inline-block;
    font-size: 14px;
    font-family: PingFangSC-Regular, PingFang SC, serif;
    font-weight: 400;
    color: #666666;
    box-sizing: border-box;
    padding: 16px 24px;
  &#125;
  .tree-list &#123;
    border-top: 1px solid #e9e9e9;
    box-sizing: border-box;
    padding: 16px 24px;
    .tree-filter &#123;
      display: flex;
      margin-bottom: 24px;
      .el-input__inner &#123;
        height: 36px;
        background: #ffffff;
        border-radius: 2px;
        border: 1px solid #d9d9d9;
      &#125;
      .el-button &#123;
        width: 32px;
        height: 36px;
        background: #ffffff;
        border-radius: 2px;
        border: 1px solid #d9d9d9;
        padding: 0 5px;
        margin-left: 10px;
      &#125;
    &#125;
    .tree-all &#123;
      color: #666666;
      height: 26px;
      line-height: 26px;
      &-iscurrent &#123;
        background-color: #edf6ff !important;
      &#125;
    &#125;
    .tree-all:hover &#123;
      background-color: #f5f7fa;
    &#125;
    .tree-content &#123;
      height: 500px;
      overflow: auto;
    &#125;
    .has-key-word-style &#123;
      background-color: #d5ebfc;
    &#125;
  &#125;
&#125;
</style>

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            