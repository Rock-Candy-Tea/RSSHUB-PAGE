
---
title: 'Vue2 to Composition API 转换器发布！助力升级Script setup'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-d45a598afc978d43da7fca634a2c65f7ec4.png'
author: 开源中国
comments: false
date: Wed, 13 Jul 2022 08:55:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-d45a598afc978d43da7fca634a2c65f7ec4.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h2>Vue2 Opitons api to Vue 3 Composition api</h2> 
<h2><img alt src="https://oscimg.oschina.net/oscnet/up-d45a598afc978d43da7fca634a2c65f7ec4.png" referrerpolicy="no-referrer"></h2> 
<h2>在线使用</h2> 
<p><strong>网站</strong></p> 
<p><a href="http://wd3322.gitee.io/to-vue3/">Gitee: vue2-to-composition-api</a></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwd3322.github.io%2Fto-vue3%2F" target="_blank">Github: vue2-to-composition-api</a></p> 
<p>随着Vue2.7版本的发布，对与Vue2用户群体从Options API 转向Composition API 有着巨大的推动作用，<code>vue2-to-composition-api</code> 是一款可以将Options API转换成Composition API的在线应用工具，转换后直接导出 <code>Script setup</code> 内容，帮助Vue2项目减少Options API语法迁移成本</p> 
<p><strong>注意事项</strong></p> 
<ul> 
 <li><code>Template</code> 中的内容不在转换器解析范畴内，需要手工替换 <code>Data</code> 数据源</li> 
 <li><code>Mixin</code>、<code>Component</code> 等外部内容无法被解析，转换前需将其剔除</li> 
 <li>转换后仍然留下<code>this.</code>指向的都是未知来源的数据</li> 
 <li>如果你使用了被Vue3废弃的指令，如 <code>$on</code>、<code>$once</code>、<code>$off</code> 等，都需要手工进行移除，转换器仍然会指向vm实例下</li> 
 <li>转化工具在设计思路上，对Vue2.7版本会更加友好，其他问题详见网站文档或本文下方</li> 
</ul> 
<h2>Props / Data 数据转换</h2> 
<p><img src="https://oscimg.oschina.net/oscnet/up-bd614bf814596b519a8e29c21c86b49febd.png" referrerpolicy="no-referrer"></p> 
<h2>Computed 计算器属性转换</h2> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-1cae1ee4607e39b0a0edcbc5a5c97bf9ff3.png" referrerpolicy="no-referrer"></p> 
<h2>Watch 侦听器转换</h2> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-23069519bd0fd3cb3e06c54f270c2582eb8.png" referrerpolicy="no-referrer"></p> 
<h2>Life cycle 生命周期转换</h2> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-fdb331a495a50f7966454954793798d5849.png" referrerpolicy="no-referrer"></p> 
<h2>Methods 方法转换</h2> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-065006a9792b9b0fcf18ba493a3064796a8.png" referrerpolicy="no-referrer"></p> 
<h2>Install 安装（推荐使用在线网站）</h2> 
<pre><code class="language-node">npm install vue2-to-composition-api
</code></pre> 
<h2>Conversion 使用转换</h2> 
<pre><code class="language-javascript">import Vue2ToCompositionApi from 'vue2-to-composition-api'

const vue2ScriptContentStr = `
export default &#123;
  name: 'Sample',
  props: &#123;
    userInfo: &#123;
      type: Object,
      required: false,
      default: () => (&#123;
        userName: 'Todd Cochran',
        userAge: 20
      &#125;)
    &#125;
  &#125;,
  data() &#123;
    return &#123;
      firstName: '',
      lastName: ''
    &#125;
  &#125;
&#125;`
const vue3ScriptContentStr = Vue2ToCompositionApi(vue2ScriptContentStr)
console.log('Hello! Composition API\\n', vue3ScriptContentStr)
</code></pre> 
<h2>无法解析的内容</h2> 
<p>请不要键入 <code>Mixin</code>、<code>Component</code> 等外部内容，转换器无法解析外部的文件，<code>Mixin</code> 混入内部的变量与方法都需另外手工处理，动态变量或者拼接的内容也同样无法被解析或解析错误</p> 
<pre><code class="language-javascript">export default &#123;
  name: 'Sample',
  mixins: [myMixin],
  components: &#123; Echart &#125;,
  methods: &#123;
    onSubmit(propName) &#123;
      this[propName] = '123'
      this.$emit(propName + '-change')
    &#125;
  &#125;
&#125;
</code></pre> 
<h2>Template中的Data变更</h2> 
<p>转换后需为 <code>Template</code> 中的 <code>Data</code> 数据需加上 <code>.data</code> 前缀，其原因是许多开发者在Options API语法中做了改变引用类型数据地址的行为（如下），<code>Data</code> 将会被转换为一个完整的对象以兼容此类操作，此方式额外产生的迭代成本更小</p> 
<p><strong>Options API:</strong></p> 
<pre><code class="language-html"><template>
  <div>&#123;&#123; userInfo &#125;&#125;</div>
</template>
</code></pre> 
<pre><code class="language-javascript">export default &#123;
  name: 'Sample',
  data() &#123;
    return &#123;
      userInfo: &#123;&#125;
    &#125;
  &#125;,
  created() &#123;
    this.userInfo = &#123; name: 'Casey Adams', age: 80 &#125;
  &#125;
&#125;
</code></pre> 
<p><strong>Composition API:</strong></p> 
<pre><code class="language-html"><template>
  <div>&#123;&#123; data.userInfo &#125;&#125;</div>
</template>
</code></pre> 
<pre><code class="language-javascript">import &#123; reactive &#125; from 'vue'

const data = reactive(&#123;
  userInfo: &#123;&#125;
&#125;)

data.userInfo = &#123; name: 'Casey Adams', age: 80 &#125;
</code></pre> 
<h2>Template中的Filter变更</h2> 
<p><code>Filter</code> 已经被废弃，它将会被转换为外部的 <code>Function</code> 内容，需要在 <code>Template</code> 中改变 <code>Filter</code> 的调用方式</p> 
<p><strong>Options API</strong></p> 
<pre><code class="language-html"><template>
  <div>&#123;&#123; married | toMarried &#125;&#125;</div>
</template>
</code></pre> 
<pre><code class="language-javascript">export default &#123;
  name: 'Sample',
  filters: &#123;
    toMarried(value) &#123;
      return value ? 'Yes' : 'No'
    &#125;
  &#125;
&#125;
</code></pre> 
<p><strong>Composition API:</strong></p> 
<pre><code class="language-html"><template>
  <div>&#123;&#123; toMarried(data.married) &#125;&#125;</div>
</template>
</code></pre> 
<pre><code class="language-javascript">function toMarried(value) &#123;
  return value ? 'Yes' : 'No'
&#125;
</code></pre> 
<h2>Vue2.7中延用Router3.x、Vuex3.x</h2> 
<p>如若不想在 <code>Vue2.7</code> 项目中更新 <code>Router4</code> 与 <code>Vuex4</code> ，可以从 <code>vue</code> 实例中获取 <code>Router</code>、<code>Router</code>、<code>Store</code></p> 
<pre><code class="language-javascript">import &#123; getCurrentInstance &#125; from 'vue'

const $vm = getCurrentInstance()
const router = $vm.proxy.$router
const route = $vm.proxy.$route
const store = $vm.proxy.$store
</code></pre> 
<hr> 
<p><strong>Git地址</strong></p> 
<p><a href="https://gitee.com/wd3322/vue2-to-composition-api">Gitee</a></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwd3322%2Fvue2-to-composition-api" target="_blank">Github</a></p>
                                        </div>
                                      
</div>
            