
---
title: '手摸手，带你尝鲜 naiveui 撸 admin 骨架（核心骨架篇）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35bd69c2d17845bb93ebe0162b18f110~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 16:21:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35bd69c2d17845bb93ebe0162b18f110~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>根据以往几篇手摸手系列文章发布，以及粉丝私信反馈，多数还是希望实例直接上代码，方便复制粘贴，这个确实是个不好的习惯哈，俗话说自己动起手来，发现问题才能解决问题嘛。</p>
<p><strong>App.vue</strong></p>
<p>说明：首先从app.vue开始，由于<strong>naiveui框架，</strong> 几个提示类型的组件（Dialog，Loading Bar，等），都需要把模板在app中引入，并且需要<strong>RouterView</strong>同级或者父级，方可优雅使用组件。</p>
<p>其次：如果你想在js中优雅地使用，也是一个问题，官方文档例子，只支持<strong>setup</strong>中使用，咋办这不科学啊，别急，上有政策下有对策，看我慢慢道来。</p>
<hr>
<pre><code class="copyable"><template>
  <NConfigProvider>
    <AppProvider>
      <RouterView />
    </AppProvider>
  </NConfigProvider>
</template>
<script lang="ts">
  import &#123; defineComponent &#125; from 'vue';
  import &#123; AppProvider &#125; from '@/components/Application';
  export default defineComponent(&#123;
    name: 'App',
    components: &#123; AppProvider &#125;,
    setup() &#123;
    &#125;
  &#125;)
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上用一个，<strong>AppProvider</strong>组件包裹<strong>RouterView，</strong> 为了实现组件引入嵌套问题，<strong>AppProvider</strong>组件实现代码如下：</p>
<pre><code class="copyable"><template>
  <n-loading-bar-provider>
    <n-dialog-provider>
      <DialogContent />
      <n-notification-provider>
        <n-message-provider>
          <MessageContent />
          <slot slot="default"></slot>
        </n-message-provider>
      </n-notification-provider>
    </n-dialog-provider>
  </n-loading-bar-provider>
</template>

<script lang="ts">
  import &#123; defineComponent &#125; from 'vue';
  import &#123;
    NDialogProvider,
    NNotificationProvider,
    NMessageProvider,
    NLoadingBarProvider,
  &#125; from 'naive-ui';
  import &#123; MessageContent &#125; from '@/components/MessageContent';
  import &#123; DialogContent &#125; from '@/components/DialogContent';

  export default defineComponent(&#123;
    name: 'Application',
    components: &#123;
      NDialogProvider,
      NNotificationProvider,
      NMessageProvider,
      NLoadingBarProvider,
      MessageContent,
      DialogContent,
    &#125;,
    setup() &#123;
      return &#123;&#125;;
    &#125;,
  &#125;);
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解释一下， <strong></strong> 相当于app.vue中的 <strong>RouterView，</strong> 以上组件必须这么用，才能在<strong>setup</strong>中正常使用。</p>
<p><strong>Layout介绍</strong></p>
<p>这是整个后台骨架核心入口模板，就是登录之后的页面，通常会包含，左侧菜单导航，顶部，内容区域，如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35bd69c2d17845bb93ebe0162b18f110~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a></p>
<p>实现<strong>Layout</strong></p>
<p>这里直接用框架提供的，layout组件，自带了折叠，深色，固定定位，等功能，相对来说是非常方便，改动样式很少即可实现一个骨架。</p>
<pre><code class="copyable"><template>
  <NLayout class="layout" :position="fixedMenu" has-sider>
    <!-- 左侧区域 -->
    <NLayoutSider>
      <!-- logo -->
      <Logo :collapsed="collapsed" />
      <!-- 左侧菜单 -->
      <AsideMenu v-model:collapsed="collapsed" v-model:location="getMenuLocation" />
    </NLayoutSider>
    <!-- 右侧区域-->
    <NLayout>
      <!-- header区域-->
      <NLayoutHeader :inverted="getHeaderInverted" :position="fixedHeader">
        <PageHeader v-model:collapsed="collapsed" :inverted="inverted" />
      </NLayoutHeader>
      <!-- 页面内容区域-->
      <NLayoutContent>
        <!-- 多标签组件-->
        <TabsView v-if="isMultiTabs" v-model:collapsed="collapsed" />
        <!-- 主内容组件-->
        <MainView />
      </NLayoutContent>
    </NLayout>
  </NLayout>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终实现的效果如下，</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6bc2f6991be54b35a784d013197343aa~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a></p>
<p>以上核心骨架和组件拆分，就已经规划完成，接下来只需要填充对应的组件内容即可</p>
<p><strong>AsideMenu组件</strong></p>
<p>菜单组件封装，包含垂直菜单，和水平菜单，实现如下：</p>
<pre><code class="copyable"><template>
  <NMenu
    :options="menus"
    :inverted="inverted"
    :mode="mode"
    :collapsed="collapsed"
    :collapsed-width="64"
    :collapsed-icon-size="20"
    :indent="24"
    :expanded-keys="openKeys"
    :value="getSelectedKeys"
    @update:value="clickMenuItem"
    @update:expanded-keys="menuExpanded"
  />
</template>

<script lang="ts">
  import &#123; defineComponent, ref, onMounted, reactive, computed, watch, toRefs, unref &#125; from 'vue';
  import &#123; useRoute, useRouter &#125; from 'vue-router';
  import &#123; useAsyncRouteStore &#125; from '@/store/modules/asyncRoute';
  import &#123; generatorMenu, generatorMenuMix &#125; from '@/utils';
  import &#123; useProjectSettingStore &#125; from '@/store/modules/projectSetting';
  import &#123; useProjectSetting &#125; from '@/hooks/setting/useProjectSetting';

  export default defineComponent(&#123;
    name: 'Menu',
    components: &#123;&#125;,
    props: &#123;
      mode: &#123;
        // 菜单模式
        type: String,
        default: 'vertical',
      &#125;,
      collapsed: &#123;
        // 侧边栏菜单是否收起
        type: Boolean,
      &#125;,
      //位置
      location: &#123;
        type: String,
        default: 'left',
      &#125;,
    &#125;,
    emits: ['update:collapsed'],
    setup(props, &#123; emit &#125;) &#123;
      // 当前路由
      const currentRoute = useRoute();
      const router = useRouter();
      const asyncRouteStore = useAsyncRouteStore();
      const settingStore = useProjectSettingStore();
      const menus = ref<any[]>([]);
      const selectedKeys = ref<string>(currentRoute.name as string);
      const headerMenuSelectKey = ref<string>('');

      const &#123; getNavMode &#125; = useProjectSetting();

      const navMode = getNavMode;

      // 获取当前打开的子菜单
      const matched = currentRoute.matched;

      const getOpenKeys = matched && matched.length ? matched.map((item) => item.name) : [];

      const state = reactive(&#123;
        openKeys: getOpenKeys,
      &#125;);

      const inverted = computed(() => &#123;
        return ['dark', 'header-dark'].includes(settingStore.navTheme);
      &#125;);

      const getSelectedKeys = computed(() => &#123;
        let location = props.location;
        return location === 'left' || (location === 'header' && unref(navMode) === 'horizontal')
          ? unref(selectedKeys)
          : unref(headerMenuSelectKey);
      &#125;);

      // 监听分割菜单
      watch(
        () => settingStore.menuSetting.mixMenu,
        () => &#123;
          updateMenu();
          if (props.collapsed) &#123;
            emit('update:collapsed', !props.collapsed);
          &#125;
        &#125;
      );

      // 监听菜单收缩状态
      watch(
        () => props.collapsed,
        (newVal) => &#123;
          state.openKeys = newVal ? [] : getOpenKeys;
          selectedKeys.value = currentRoute.name as string;
        &#125;
      );

      // 跟随页面路由变化，切换菜单选中状态
      watch(
        () => currentRoute.fullPath,
        () => &#123;
          updateMenu();
          const matched = currentRoute.matched;
          state.openKeys = matched.map((item) => item.name);
          const activeMenu: string = (currentRoute.meta?.activeMenu as string) || '';
          selectedKeys.value = activeMenu ? (activeMenu as string) : (currentRoute.name as string);
        &#125;
      );

      function updateMenu() &#123;
        if (!settingStore.menuSetting.mixMenu) &#123;
          menus.value = generatorMenu(asyncRouteStore.getMenus);
        &#125; else &#123;
          //混合菜单
          const firstRouteName: string = (currentRoute.matched[0].name as string) || '';
          menus.value = generatorMenuMix(asyncRouteStore.getMenus, firstRouteName, props.location);
          const activeMenu: string = currentRoute?.matched[0].meta?.activeMenu as string;
          headerMenuSelectKey.value = (activeMenu ? activeMenu : firstRouteName) || '';
        &#125;
      &#125;

      // 点击菜单
      function clickMenuItem(key: string) &#123;
        if (/http(s)?:/.test(key)) &#123;
          window.open(key);
        &#125; else &#123;
          router.push(&#123; name: key &#125;);
        &#125;
      &#125;

      //展开菜单
      function menuExpanded(openKeys: string[]) &#123;
        if (!openKeys) return;
        const latestOpenKey = openKeys.find((key) => state.openKeys.indexOf(key) === -1);
        const isExistChildren = findChildrenLen(latestOpenKey as string);
        state.openKeys = isExistChildren ? (latestOpenKey ? [latestOpenKey] : []) : openKeys;
      &#125;

      //查找是否存在子路由
      function findChildrenLen(key: string) &#123;
        if (!key) return false;
        const subRouteChildren: string[] = [];
        for (const &#123; children, key &#125; of unref(menus)) &#123;
          if (children && children.length) &#123;
            subRouteChildren.push(key as string);
          &#125;
        &#125;
        return subRouteChildren.includes(key);
      &#125;

      onMounted(() => &#123;
        updateMenu();
      &#125;);

      return &#123;
        ...toRefs(state),
        inverted,
        menus,
        selectedKeys,
        headerMenuSelectKey,
        getSelectedKeys,
        clickMenuItem,
        menuExpanded,
      &#125;;
    &#125;,
  &#125;);
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码实现比较简单，官方提供的<strong>menu</strong>组件，会自动帮我们递归创建出子菜单，这里我们只需把数据丢给他即可，真是大快人心啊。</p>
<p>说一下核心的2个方法：</p>
<p>1、左侧普通菜单</p>
<pre><code class="copyable">/**
 * 递归组装菜单格式
 */
export function generatorMenu(routerMap: Array<any>) &#123;
  return filterRouter(routerMap).map((item) => &#123;
    const isRoot = isRootRouter(item);
    const info = isRoot ? item.children[0] : item;
    const currentMenu = &#123;
      ...info,
      ...info.meta,
      label: info.meta?.title,
      key: info.name,
    &#125;;
    // 是否有子菜单，并递归处理
    if (info.children && info.children.length > 0) &#123;
      // Recursion
      currentMenu.children = generatorMenu(info.children);
    &#125;
    return currentMenu;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里通过路由对象数组，组装成<strong>menu</strong>组件需要的格式，并且还可以自定义一些逻辑在这里实现</p>
<p>2、顶部菜单模式-混合菜单</p>
<pre><code class="copyable">/**
 * 混合菜单
 * */
export function generatorMenuMix(routerMap: Array<any>, routerName: string, location: string) &#123;
  const cloneRouterMap = cloneDeep(routerMap);
  const newRouter = filterRouter(cloneRouterMap);
  if (location === 'header') &#123;
    const firstRouter: any[] = [];
    newRouter.forEach((item) => &#123;
      const isRoot = isRootRouter(item);
      const info = isRoot ? item.children[0] : item;
      info.children = undefined;
      const currentMenu = &#123;
        ...info,
        ...info.meta,
        label: info.meta?.title,
        key: info.name,
      &#125;;
      firstRouter.push(currentMenu);
    &#125;);
    return firstRouter;
  &#125; else &#123;
    return getChildrenRouter(newRouter.filter((item) => item.name === routerName));
  &#125;
&#125;

/**
 * 递归组装子菜单
 * */
export function getChildrenRouter(routerMap: Array<any>) &#123;
  return filterRouter(routerMap).map((item) => &#123;
    const isRoot = isRootRouter(item);
    const info = isRoot ? item.children[0] : item;
    const currentMenu = &#123;
      ...info,
      ...info.meta,
      label: info.meta?.title,
      key: info.name,
    &#125;;
    // 是否有子菜单，并递归处理
    if (info.children && info.children.length > 0) &#123;
      // Recursion
      currentMenu.children = getChildrenRouter(info.children);
    &#125;
    return currentMenu;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里也是为<strong>menu</strong>组件提供数据支持</p>
<p><strong>PageHeader组件</strong></p>
<p>这个组件主要是实现了这些功能，比较简单，而且不一定是你想要的，所以不说了哈~</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e13c5fb53374467587f0e4734f79ba8a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a></p>
<p><strong>TabsView</strong></p>
<p>多标签页，实现的功能比较多，后面单独抽一起来解析，手摸手带你撸。</p>
<p><strong>MainView</strong></p>
<pre><code class="copyable"><template>
  <RouterView>
    <template #default="&#123; Component, route &#125;">
      <transition name="zoom-fade" mode="out-in" appear>
        <keep-alive v-if="keepAliveComponents" :include="keepAliveComponents">
          <component :is="Component" :key="route.fullPath" />
        </keep-alive>
        <component v-else :is="Component" :key="route.fullPath" />
      </transition>
    </template>
  </RouterView>
</template>

<script>
  import &#123; defineComponent, computed &#125; from 'vue';
  import &#123; useAsyncRouteStore &#125; from '@/store/modules/asyncRoute';

  export default defineComponent(&#123;
    name: 'MainView',
    components: &#123;&#125;,
    props: &#123;
      notNeedKey: &#123;
        type: Boolean,
        default: false,
      &#125;,
      animate: &#123;
        type: Boolean,
        default: true,
      &#125;,
    &#125;,
    setup() &#123;
      const asyncRouteStore = useAsyncRouteStore();
      // 需要缓存的路由组件
      const keepAliveComponents = computed(() => asyncRouteStore.keepAliveComponents);
      return &#123;
        keepAliveComponents,
      &#125;;
    &#125;,
  &#125;);
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里主要是做一个缓存路由，和动画效果，以及公共布局风格统一处理</p>
<h1 data-id="heading-1">最后上成品</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c31a38a9356549caa07195865931ebac~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a></p>
<p>以上只展示一些核心代码，和思路，想看完整代码，可找一下，naive-ui-admin 官方仓库</p></div>  
</div>
            