
---
title: 'Electron+Vue3 MAC 版日历开发记录(20)——彻底去除PrimeVue'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 20 Jun 2021 06:03:57 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第20天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74b12c9f69fb459490c4f92fcb2207ce~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>开篇之前的叨叨，今天看到掘金伙伴的评论，还是有点小小激动，毕竟不是自己擅长的开发语言，项目也是因为这次掘金的活动而突发想着把开发过程记录下来。所以能得到关注，我还是感谢这位小伙伴～</p>
<p>但愿项目记录对大家有些价值，也欢迎大家多多指正批评！</p>
<p>好了，废话不多说，开始说说今天的记录内容。</p>
<p>今天看了看 <a href="https://fossa.com/" target="_blank" rel="nofollow noopener noreferrer"><code>fossa</code></a> 引入插件数量：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fac8716cbc194ad8829b80ab11c28337~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>感觉还是引入的有点多，就这么个小项目。所以接下来还是要考虑如何减少第三方插件的不价值引入。今天彻底把 <code>Primevue</code> 移除。</p>
<h2 data-id="heading-0">重构--彻底去除 <code>primevue</code></h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/070bf166f80742119c00eff91cba047f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">天气小布局</h3>
<p>没想好怎么使用天气这个小布局，之前单独成一个组件，是为了后续看看如何扩展使用，所以重构起来比较简单：</p>
<pre><code class="copyable"><template>
  <n-badge
    :value="temp"
    class="weather"
  >
    <n-image
      width="40"
      :src="weatherIcon"
    />
  </n-badge>
</template>

<script lang="ts">
import &#123; defineComponent&#125; from 'vue';
import &#123; NBadge, NImage &#125; from 'naive-ui';
import weathericons from '~/images/weathericons/100.png';
<span class="copy-code-btn">复制代码</span></code></pre>
<p>没什么可说的，直接用一个 <code>NBadge</code> 组件解决。</p>
<h3 data-id="heading-2">创建事件组件</h3>
<pre><code class="copyable"><template>
  <Dialog
    v-model:visible="eventDialogVisible"
    :modal="true"
    @click="$emit('update:visibleFullDialog', eventDialogVisible)"
  >
    <div class="p-fluid">
      <span class="p-float-label">
        <InputText
          id="eventInput"
          v-model="eventText"
          type="text"
        />
        <label for="eventInput">事件内容</label>
      </span>
    </div>
    <div class="p-fluid p-formgrid p-grid">
      <Calendar
        id="range"
        v-model="dates"
        date-format="MM d,yy"
        ::minDate="Date()"
        selection-mode="range"
        :inline="true"
      />
    </div>
    <template #footer>
      <Button
        label="取消"
        icon="pi pi-times"
        class="p-button-danger"
        @click="$emit('update:visibleFullDialog', false)"
      />
      <Button
        label="确定"
        icon="pi pi-check"
        autofocus
        @click="add"
      />
    </template>
  </Dialog>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>核心的主要使用：<code>Dialog</code>、<code>InputText</code>、<code>Calendar</code>:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9bc15e776b6459d99608f6cc6effdcf~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面使用 Naive UI 找出对应的重构：</p>
<pre><code class="copyable"><template>
  <n-drawer-content
    title="创建事件"
    closable
  >
    <n-space vertical>
      <n-input
        id="eventInput"
        v-model:value="eventText"
        placeholder="事件内容"
      />
      <n-date-picker
        v-model:value="dates"
        type="daterange"
        :actions="['confirm']"
        clearable
      />
    </n-space>
    <template #footer>
      <n-button
        type="success"
        @click="add"
      >
        增加
      </n-button>
    </template>
  </n-drawer-content>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad1067b602154a128349e91d9899a855~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">主界面</h2>
<p>主界面主要是最后一个下拉菜单了：</p>
<pre><code class="copyable">  <Menu
    id="overlay_tmenu"
    ref="menu"
    :model="items"
    :popup="true"
  />
  ...
  import Menu from 'primevue/menu';
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个直接使用 <code>Naive UI</code> 的下拉菜单解决：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b1a7d328d694728a37bb948291b7859~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">  <n-dropdown
    trigger="hover"
    placement="bottom-start"
    :options="options"
    @select="dropdownClick"
  >
    <n-button
      text
      type="success"
      :keyboard="false"
      class="dropdown"
    >
      <n-icon>
        <list-icon />
      </n-icon>
    </n-button>
  </n-dropdown>
  
  ...
  
  import &#123; NDropdown, NDrawer, NDrawerContent, NButton, NIcon &#125; from 'naive-ui';
import &#123; List as ListIcon, PowerOff as PowerOffIcon &#125; from '@vicons/fa';

options: [
&#123;
  label: '创建事件',
  key: 'goCreateEventView',
  icon() &#123;
    return h(NIcon, null, &#123;
      default: () => h(Add12FilledIcon),
    &#125;);
  &#125;,
  on: this.goCreateEventView,
&#125;,
&#123;
  label: '设置',
  key: 'goSettingView',
  icon() &#123;
    return h(NIcon, null, &#123;
      default: () => h(LauncherSettings24FilledIcon),
    &#125;);
  &#125;,
  on: this.goSettingView,
&#125;,
&#123;
  type: 'divider',
  key: 'd1',
&#125;,
&#123;
  label: '退出应用',
  key: 'quit',
  icon() &#123;
    return h(NIcon, null, &#123;
      default: () => h(PowerOffIcon),
    &#125;);
  &#125;,
  on: this.quit,
&#125;,
],
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个代码基本参考官网文档来的，没出现什么问题，此外之前的操作按钮用的是 <code>Fullcalendar</code> 自定义按钮，这次也把他们移除了(为后续自定义日历组件做准备)：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd6b1981d2ab4ea199b3a8929ccdb97f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>执行看看效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb8cbe418bc049a29f7da30ac23bc708~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>到此，基本把所有该用到的地方都改过来了，最后就剩下引用了。</p>
<h2 data-id="heading-4">移除所有引用</h2>
<pre><code class="copyable">// index.ts
import PrimeVue from 'primevue/config';
import ToastService from 'primevue/toastservice';
import 'primevue/resources/themes/saga-green/theme.css';
import 'primevue/resources/primevue.min.css';
import 'primeicons/primeicons.css';

// package.json
"primeflex": "^2.0.0",
"primeicons": "^4.1.0",
"primevue": "3.3.5",
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">小结</h2>
<p>最后我们重新 <code>yarn upgrade</code> 生成新的 <code>yarn.lock</code> 文件以供 Github Action 自动打包服务。</p>
<p>今天刚好第二十天，基本完成该有的逻辑和代码了，剩下的 10 天就是把每一个功能和模块好好排查问题，把 Test 测试用例补上，以及参考主流的开源项目把该有得补上，至少还有以下几个内容没完成：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d093aaaab90b402fa7774075cfa85e30~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后，看看依赖项少了 3 个：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ef564af187642758eee7aa1947afdb9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>代码已同步到 github 上了：<a href="https://github.com/fanly/fanlymenu" target="_blank" rel="nofollow noopener noreferrer">github.com/fanly/fanly…</a></p>
</blockquote></div>  
</div>
            