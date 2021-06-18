
---
title: 'Electron+Vue3 MAC 版日历 开发记录(17)——使用 Naive UI重构黄历页面'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 07:26:19 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第17天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844c86d5923d4420bf0b7f3cec1b8d92~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>把昨天的扫尾工作做完，整个 <code>Setting</code> 页面替换了，完整代码如下：</p>
<pre><code class="copyable"> <template>
  <n-space vertical>
    <h4>显示节假日</h4>
    <n-switch
      v-model:value="inputSwitchFestivalsModel"
      size="large"
      @update-value="updateFestivalsModel"
    />
    <h4>显示天气预报</h4>
    <n-switch
      v-model:value="inputSwitchWeatherModel"
      size="large"
      @update-value="updateWeatherModel"
    />
    <n-space
      v-if="inputSwitchWeatherModel"
      inline
    >
      <n-input-number
        v-model:value="longitude"
        :min="-180"
        :max="180"
        :show-button="false"
        placeholder="经度"
        @update:value="changeLocalLocation"
      />
      <n-input-number
        v-model:value="latitude"
        :min="-90"
        :max="90"
        :show-button="false"
        placeholder="纬度"
        @update:value="changeLocalLocation"
      />
    </n-space>
    <n-divider dashed>
      专注设置
    </n-divider>
    <n-space vertical>
      <n-slider
        v-model:value="focus_time"
        :step="5"
        :min="5"
        :max="120"
      />
      <n-button
        type="primary"
        size="large"
        @click="focus"
      >
        <template #icon>
          <n-icon>
            <caret-right-icon />
          </n-icon>
        </template>
        &#123;&#123; focusLabel &#125;&#125;
      </n-button>
    </n-space>
  </n-space>
</template>

<script lang="ts">
import &#123; defineComponent&#125; from 'vue';
import &#123; useStore &#125; from '/@/store';
import &#123; NSpace, NSwitch, NInputNumber, NButton, NIcon, NSlider, NDivider &#125; from 'naive-ui';
import &#123; CaretRight as CaretRightIcon &#125; from '@vicons/fa';

export default defineComponent(&#123;
  name: 'SettingSub',
  components: &#123;
    NSpace,
    NSwitch,
    NInputNumber,
    NButton,
    NIcon,
    CaretRightIcon,
    NSlider,
    NDivider,
  &#125;,
  props: &#123;
    changeShowFestivals: Boolean,
    changeShowWeather: Boolean,
    location: Object,
  &#125;,
  emits: [
    'focusClick',
    'update:visibleFullSetting',
    'update:changeShowFestivals',
    'update:changeShowWeather',
    'update:location',
  ],
  setup() &#123;
    const store = useStore();
    return &#123;
      store,
    &#125;;
  &#125;,
  data() &#123;
    return &#123;
      inputSwitchFestivalsModel: this.changeShowFestivals,
      inputSwitchWeatherModel: this.changeShowWeather,
      longitude: this.location?.longitude,
      latitude: this.location?.latitude,
      focus_time: 40,
    &#125;;
  &#125;,
  computed: &#123;
    // 计算属性的 getter
    focusLabel(): string &#123;
      return '开始专注' + this.focus_time + '分钟';
    &#125;,
  &#125;,
  mounted() &#123;
    this.focus_time = this.store.state.focusTime;
  &#125;,
  methods: &#123;
    updateFestivalsModel(value: boolean): void &#123;
      this.$emit('update:changeShowFestivals', value);
    &#125;,
    updateWeatherModel(value: boolean): void &#123;
      this.$emit('update:changeShowWeather', value);
    &#125;,
    changeLocalLocation(): void &#123;
      this.$emit('update:location', &#123;
        'longitude': this.longitude,
        'latitude': this.latitude,
      &#125;);
    &#125;,
    focus(): void &#123;
      this.store.commit('changeFocusTime', this.focus_time);
      this.$emit('focusClick');
      window.electron.ipcRenderer.send('show-focus-window');
    &#125;,
  &#125;,
&#125;);
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这里我用的 <code>NSwitch</code> 想把经纬度的输入框隐藏了，用的 <code>v-show</code> 发现我点「显示农历」也能把这个隐藏去掉，这是个 bug，后来我改为用 <code>v-if</code>：</p>
</blockquote>
<pre><code class="copyable"><n-space
  v-if="inputSwitchWeatherModel"
  inline
>
  ...
</n-space>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>整体感觉看起来还不错的样子：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be6b46d5a7ec4edcae9c53a3423bae24~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中我用的<a href="https://www.naiveui.com/zh-CN/os-theme/components/drawer" target="_blank" rel="nofollow noopener noreferrer">「抽屉」组件</a> 代替之前的 <code>Sidebar</code> 组件，但 <code>NDrawer</code> 组件没有「关闭按钮」功能，只能通过上层点击，所以把这个放在了 <code>Main</code> 主界面。</p>
<pre><code class="copyable"><n-drawer
  v-model:show="visibleFullSetting"
  :width="drawerWidth"
  placement="left"
>
  <n-drawer-content title="设置">
    <setting-sub
      v-model:changeShowWeather="changeShowWeather"
      v-model:changeShowFestivals="changeShowFestivals"
      v-model:location="location"
      @focusClick="focusClick"
    />
  </n-drawer-content>
</n-drawer>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-0">黄历页面</h2>
<p>第二个开始调整的「黄历页面」。动 ta 的理由比较简单，因为 ta 使用了布局了。</p>
<p>我先放改好的代码出来：</p>
<pre><code class="copyable"><template>
  <n-layout has-sider :style="layoutStyle">
    <n-layout-sider bordered :width="150">
      <n-grid x-gap="6" :cols="2" style="height: 100%;">
        <n-gi>
          <div class="nongliString">
            &#123;&#123; lunarData.nongliString &#125;&#125;
          </div>
        </n-gi>
        <n-gi style="padding: 40px 0;">
          <div
            v-for="item in lunarData.ganzhi"
            :key="item"
            class="onecn"
          >
            &#123;&#123; item &#125;&#125;
          </div>
        </n-gi>
      </n-grid>
    </n-layout-sider>
    <n-layout :style="layoutStyle">
      <n-layout-header bordered>
        <div>
          <n-tag
            type="success"
          >
            宜
          </n-tag>
          <n-tag
            v-for="item in lunarData.yi"
            :key="item"
            type="success"
          >
            &#123;&#123; item &#125;&#125;
          </n-tag>
        </div>
      </n-layout-header>
      <n-layout-content content-style="padding: 24px; ">
        &#123;&#123; lunarData.yangliString &#125;&#125;
      </n-layout-content>
      <n-layout-footer bordered position="absolute">
        <div>
          <n-tag
            type="error"
            round
          >
            忌
          </n-tag>
          <n-tag
            v-for="item in lunarData.ji"
            :key="item"
            type="error"
            round
          >
            &#123;&#123; item &#125;&#125;
          </n-tag>
        </div>
      </n-layout-footer>
    </n-layout>
  </n-layout>
</template>

<script lang="ts">
import &#123; defineComponent, ref &#125; from 'vue';
import &#123; NGrid, NGi, NLayout, NLayoutSider, NLayoutHeader, NLayoutContent, NLayoutFooter, NTag &#125; from 'naive-ui';
import LunarService from '../../../services/LunarService';

export default defineComponent(&#123;
  name: 'DateViewSub',
  components: &#123;
    NGrid,
    NGi,
    NLayout,
    NLayoutSider,
    NLayoutHeader,
    NLayoutContent,
    NLayoutFooter,
    NTag,
  &#125;,
  props: &#123;
    date: Date,
    weather: Object,
  &#125;,
  data() &#123;
    return &#123;
      layoutStyle: "height: " + (Number(import.meta.env.VITE_APP_HEIGHT) - 100) + "px;",
    &#125;;
  &#125;,
  setup(props) &#123;
    const lunarService = ref(new LunarService(props.date));
    const lunarData =  lunarService.value.getDateViewDate();
    return &#123;
      lunarData,
    &#125;;
  &#125;,
&#125;);
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
@import "~/styles/default.scss";

.nongliString &#123;
  display: flex;
  /*实现垂直居中*/
  align-items: center;
  margin: 0 auto;
  height: 100%;
  width: 2.5rem;
  font-size: 2.5em;
  color: #000;
&#125;

.onecn &#123;
  display: flex;
  /*实现垂直居中*/
  align-items: center;
  margin: 0 auto;
  width: 1.4rem;
  height: 33%;
  font-size: 1.4rem;
  color: #000;
&#125;

.n-layout-sider &#123;
  width: 150px;
&#125;
.n-layout-header &#123;
  padding: 24px;
&#125;
.n-layout-footer &#123;
  padding: 24px;
&#125;

</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里先主要用的是：<a href="https://www.naiveui.com/zh-CN/os-theme/components/layout" target="_blank" rel="nofollow noopener noreferrer"><code>NLayout</code> 布局组件</a>，左右结构：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b80baeaa2844ff89c23a3db17e64397~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>左边结构主要显示农历和农历信息，和之前的样式一样，但使用的是 <a href="https://www.naiveui.com/zh-CN/os-theme/components/grid" target="_blank" rel="nofollow noopener noreferrer"><code>NGrid</code> Grid 栅格组件</a>，将分配的布局分成左右两等分：</p>
<p>右边的结构就很简单了，主要使用的是 NLayoutHeader, NLayoutContent, NLayoutFooter, 页面上下结构，我这边上下放的是「宜」和「忌」，一样的，用的是标签组件 <code>NTag</code></p>
<p>因为使用布局组建很难调，就如作者所说的：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48b0040b42ac4508b37a401ae59472f9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是，我花了一晚上把 ta 调出来，还是挺有成就感的，让我们看看改变前后的对比吧：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f68a94fbd8f4a198f752d2192ed42ab~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>修改之后：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0983f2ac369d487091cab9c7d272e606~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>基本达到之前的效果了。</p>
<h2 data-id="heading-1">小结</h2>
<p>这是重构页面的第二天了，由于平时工作很多，不能花很多时间在这个项目上，但也在有限时间让自己学到一些东西，还是有很多值得继续学习的，我尽可能的记录有价值的东西，水分少些，欢迎大家批评指正～</p>
<p>未完待续！</p>
<blockquote>
<p>代码已同步到 github 上了：<a href="https://github.com/fanly/fanlymenu" target="_blank" rel="nofollow noopener noreferrer">github.com/fanly/fanly…</a></p>
</blockquote></div>  
</div>
            