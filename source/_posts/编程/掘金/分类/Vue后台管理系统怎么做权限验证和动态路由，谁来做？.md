
---
title: 'Vue后台管理系统怎么做权限验证和动态路由，谁来做？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6726cb879cc4eae963d7d5e0f8ad801~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 03:28:28 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6726cb879cc4eae963d7d5e0f8ad801~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h2 data-id="heading-0">吹一下水</h2>
<p>我好久都没有写过文章了，主要是因为还是觉得自己才疏学浅，如果把自己学到的东西以那种类似教程的形式写出来的话，怕误认子弟。然后自己也还没有工作，也没有什么好的工作经验可以分享。最后一个原因就是，实在是没时间，学校乱七八糟的事情一大堆，期末就忙的跟狗一样。也没怎么学新东西，然后现在感觉我已经out了，群里大佬们聊的东西已经听不懂了（其实也没那么夸张），哈哈哈，这可能就是前端人的痛吧。<br>
然后说说我为什么想起要写这篇文章吧，是因为最近打算做自己的一个商城项目，我是先做后台的，主要的前端技术栈就是Vue，后端我是用的PHP+Laravel。我做后台的时候第一个面临的问题就是权限的问题，单说权限可能太笼统了，到底是什么权限呢。其实我这个项目里面涉及到的权限包括两个，一个是<strong>操作权限</strong>，一个是<strong>路由访问权限</strong>（这里指前端路由）。我接下来就讲一下我的思路和一步一步的探索（简单粗暴的说就是踩坑历程）</p>
<h2 data-id="heading-1">思路准备</h2>
<p>首先思考权限谁来做？前端还是后端，分情况来讨论。我觉得操作权限必须是后端来做的，操作权限就是对每一个操作进行权限限制，比如超级管理员可以添加后台用户、禁用后台用户，而其他的后台用户无法进行这些操作像这么细粒度的控制最好还是由后端来做。就是对每一个接口进行权限访问控制，如果由前端来做的话可能得累死，而且不安全。第二个就是路由的访问权限，即便是我们做了细粒度的操作权限限制，可我们还是希望不同的用户登录进后台的时候能够访问的路由是不同的，拥有的菜单也是不同的。因为这样其实是提高了用户体验的，不同角色的用户拥有的菜单不同，就相当于提前防止用户误操作（因为并不清楚哪些操作有权限），好过等到用户执行某一个具体的操作，然后被告知无权限好吧。其实这也不是完全可以做到的，比如两个用户都可以访问同一个页面，但是他们在这个页面里的操作权限却是不同的，总结一下就是，后端的验证是为了保证数据完整和操作安全的，而前端做验证，不管是什么验证都是为了提高可用性和用户体验的。</p>
<p>路由的访问权限也是我主要想说的，因为操作权限，大部分都是后端做的，前端顶多是根据接口响应给用户对应的提示。我的后台是基于开源项目 <a href="https://github.com/PanJiaChen/vue-element-admin" target="_blank" rel="nofollow noopener noreferrer">vue-element-admin</a> 开发的，这个项目的路由访问控制是放在前端做的，按照花裤衩大佬的思路就是，前端有一份动态路由表，等到用户登录拿到用户的角色之后根据当前登录用户的角色去筛选出可以访问的路由，形成一份定制路由表，然后动态挂载路由。花裤衩大佬说，这样做的好处就是，前端每开发一个页面不需要让后端再去配一下路由和权限了，从而避免被后端支配，哈哈哈。</p>
<p>回到我自己的项目中。首先，我这是个人项目（可以理解为搞来玩玩的），前端和后端都是自己做，只可能自己折磨自己，当然，这不是最主要的原因。最主要的是，我这个项目中管理员是可以添加角色的，包括给角色分配权限，然后给用户分配角色。然而，路由表又是跟角色挂钩。考虑一种情况，项目上线之后，管理员添加了一个新角色，并且要给这个角色分配菜单。如果采用将路由表放在前端的话那么每个路由的可访问角色都是写死的，要给新添加的角色分配菜单，只能改前端代码，显然不是很合适。所以我才用了后者，就是把路由信息放在后端，后端将路由信息和角色关联起来，用户登录之后请求对应的接口拿到属于这个用户的路由信息（也就是菜单），然后前端对返回的数据格式化，转换成符合vue-router的路由格式，然后动态挂载。将路由信息放在后端，这样就可以对路由进行配置了，比如说超级管理员今天很不高兴，不想让某个角色下的用户访问某个路由，直接在该路由下剔除这个角色就可以了（之后会有图动态地演示这一过程），想想是不是很爽。</p>
<p>讲了这么多，不知道我表达清楚了没。小结一下，我这个项目涉及到<strong>操作权限</strong>和<strong>路由访问权限</strong>，前者完全放在后端做，把权限加到接口上。后者则需要前端和后端共同配合，接下会主要地讲我是怎样实现后者的，不会把完整的实现代码放出来，因为没必要，第一点原因是我觉得代码只是工具，重要的是思路，第二点原因我前面也提到过了，我不是很想写那种说教式教程式的文章，所以更多的是分享。只会讲一下大概的实现过程还有一些注意事项，前后端都会提到，但主要是前端。</p>
<h2 data-id="heading-2">实现过程</h2>
<p>说实话，其实在实现过程中后端是占主要地位的，像角色的匹配，路由的筛选都需要后端去做。那么后端要想做到这些，就离不开数据库和数据表，所以先来看看我设计的表吧。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6726cb879cc4eae963d7d5e0f8ad801~tplv-k3u1fbpfcp-watermark.image" alt="table.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我给出的这个数据表关系图，除了有关菜单的表，还包括所有的权限表和角色表，可以说是支撑了后端所有有关权限角色的操作。那么其实和接下来要说的内容有关的表就只有三个<code>roles</code> 、<code>menu</code> 、<code>menu_role</code>，其实并不是复杂，不要被吓到了。<code>roles</code>表用来存放整个系统的角色，<code>menu</code>表用来存放菜单信息（也就是给前端的路由），<code>menu_role</code> 表是作为一张中间表来连接 <code>menu</code> 表和 <code>roles</code> 表的。<strong>这里要补充一下就是，其实用户表和角色表也是有关联的，毕竟用户登录只能拿到用户信息，所以用户、角色、菜单这三者之间必须要有关联。也就说接下来的内容都是建立在基本的用户角色权限功能完整的情况下的</strong>。说完了表，接下来讲一下后端接口要返回的内容</p>
<h3 data-id="heading-3">1、后端接口</h3>
<p>要想知道后端该返回怎样的数据，就得先知道前端需要怎样的数据，前端需要的数据大概长这样：</p>
<pre><code class="copyable">[
  &#123;
    path: '/permission',
    component: Layout,
    redirect: '/permission/page',
    name: 'Permission',
    meta: &#123;
      title: '权限管理',
      icon: 'lock',
      roles: ['super_admin', 'editor']
    &#125;,
    children: [
      &#123;
        path: 'role',
        component: () => import('@/views/permission/role'),
        name: 'RolePermission',
        meta: &#123;
          title: '角色信息',
          roles: ['super_admin']
        &#125;
      &#125;
    ]
  &#125;,
  &#123;
    path: '/icon',
    component: Layout,
    children: [
      &#123;
        path: 'index',
        component: () => import('@/views/icons/index'),
        name: 'Icons',
        meta: &#123; title: 'Icons', icon: 'icon', noCache: true &#125;
      &#125;
    ]
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这上面放出来的数据是最理想的数据了，也就是如果后端返回这样的数据，那么前端直接用就行了。但这是不太可能的，因为可以看到我上面的数据库表有很多字段，为的就是覆盖到大多数情况，那么后端并不知道哪些东西对你前端来说是有用的，而且也不清楚数据组合的方式，要组合起来也很麻烦的，因为表是二维的，无法描述一些层级关系，最主要的是后端返回的<code>component</code>字段仅仅是前端组件的一个路径而已，前端肯定还是要转换成自定义的组件的。所以，综上所述<strong>后端只能如数返回所有的字段</strong>，而前端要自己筛选和组合数据。<br>
现在知道了后端要返回全部的字段，还有一个问题，就是路由的嵌套问题，虽然后端返回所有的字段，但是你至少得告诉前端各个路由之间的嵌套关系吧（也就是父级路由和子路由），细心的小伙伴可能看到了我上面的<code>menu</code> 表中有一个 <code>pid</code> 字段，这个字段就是用来描述路由之间的关系的，父级路由的 <code>pid</code>是 <code>0</code> 子路由的 <code>pid</code> 是父级路由在表中的 <code>id</code> 字段。把这些东西捋顺了之后，就可以写代码了，我还是贴一些后端代码出来吧。</p>
<pre><code class="hljs language-php copyable" lang="php"><span class="hljs-keyword">public</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">index</span>(<span class="hljs-params">Request <span class="hljs-variable">$request</span></span>)
</span>&#123;
    <span class="hljs-variable">$user</span> = auth(<span class="hljs-string">'admin'</span>)->user();
    <span class="hljs-comment">// 角色下的菜单id，去除重复的菜单id</span>
    <span class="hljs-variable">$menu_ids</span> = MenuRole::whereIn(<span class="hljs-string">'rid'</span>, <span class="hljs-variable">$user</span>->roles->pluck(<span class="hljs-string">'id'</span>))->distinct()->pluck(<span class="hljs-string">'mid'</span>);
    <span class="hljs-variable">$menus</span> = Menu::whereIn(<span class="hljs-string">'id'</span>, <span class="hljs-variable">$menu_ids</span>)->where(<span class="hljs-string">'pid'</span>, <span class="hljs-number">0</span>)->with([
        <span class="hljs-string">'children'</span> => <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"><span class="hljs-variable">$query</span></span>) <span class="hljs-keyword">use</span>(<span class="hljs-params"><span class="hljs-variable">$menu_ids</span></span>) </span>&#123;
            <span class="hljs-keyword">return</span> <span class="hljs-variable">$query</span>->whereIn(<span class="hljs-string">'id'</span>, <span class="hljs-variable">$menu_ids</span>);
        &#125;
    ])->get();
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">$this</span>->response->array(<span class="hljs-variable">$menus</span>->toArray());
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>熟悉Laravel的小伙伴应该很快就能看懂这段代码，不熟悉的也没关系，关注最后返回的数据也可以的。上面这段代码先筛选出用户所有角色的id（因为一个用户可能会有多个角色），然后在根据角色id去找到对应的菜单id，然后再去 <code>menu</code> 表中查出记录即可。 <strong>敲黑板</strong>！这里要注意了，有可能用户拥有的多个角色都可访问某一个路由，这个时候就要去除重复的记录，要不然最后返回给前端的数据中就会有重复的数据，最后导致在页面中出现重复的菜单。</p>
<p>返回的数据大概长这样：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16db606546e74915a1646aaa65d0a1d7~tplv-k3u1fbpfcp-watermark.image" alt="1.JPG" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">2、前端格式化路由数据</h3>
<p>终于到前端干活了，前端做的事情很简单，就是请求接口，拿到数据，格式化数据，挂载路由。一步一步来吧。</p>
<p>可能大家会觉得拿数据不是很简单吗，但是也要考虑拿数据的方式、拿数据的时机和拿到数据之后保存到哪？<br>
这里我就不卖关子了，在这个项目中是把请求放在Vuex中的action中，因为最后拿到的数据是要保存在Vuex中，以便左侧菜单组件能够拿到路由信息渲染出对应的菜单，这样做就方便一点，至于时机，是在router的beforeEach里等到用户登录之后发起请求的。还是把代码贴出来</p>
<pre><code class="copyable">file: @/api/user.js
// 获取动态路由表
export function getAsyncRoutes() &#123;
  return request(&#123;
    url: '/admin/menus',
    method: 'get'
  &#125;)
&#125;

file: @/store/modules/permission.js
import &#123; getAsyncRoutes &#125; from '@/api/user'
import formatRoutes from '@/utils/formatRoutes'
import Layout from '@/layout'
// 有些依赖就没有完全列出来
// actions
const actions = &#123;
  generateRoutes(&#123; commit &#125;) &#123;
    return new Promise(resolve => &#123;
      // 从服务器获取路由表
      getAsyncRoutes().then(routes => &#123;
        // 格式化路由表
        const accessedRoutes = formatRoutes(routes, Layout)  // formatRoutes函数会在后面放出来
        // 将路由保存到Vuex中
        commit('SET_ROUTES', accessedRoutes)
        resolve(accessedRoutes)
      &#125;)
    &#125;)
  &#125;
&#125;

export default &#123;
  namespaced: true,
  state,
  mutations,
  actions
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码只是定义了action，接下来就需要在vue-router的路由钩子里面，dispath定义好的action就可以拿到格式化好的数据了</p>
<pre><code class="copyable">import router from './router'
import store from './store'
import &#123; Message &#125; from 'element-ui'
import NProgress from 'nprogress'
import 'nprogress/nprogress.css'
import &#123; getToken &#125; from '@/utils/auth'
import getPageTitle from '@/utils/get-page-title'

NProgress.configure(&#123; showSpinner: false &#125;)

const whiteList = ['/login', '/auth-redirect']

router.beforeEach(async(to, from, next) => &#123;
  // 开启页面进度条
  NProgress.start()

  // 设置标题
  document.title = getPageTitle(to.meta.title)

  const hasToken = getToken()
  if (hasToken) &#123;
    if (to.path === '/login') &#123;
      // 已登录，跳转到: '/'
      next(&#123; path: '/' &#125;)
      NProgress.done() // 关闭页面进度条
    &#125; else &#123;
      // 是否通过用户信息拿到角色信息
      const hasRoles = store.getters.roles && store.getters.roles.length > 0
      if (hasRoles) &#123;
        // 登录过并且有角色信息，直接进入下一个路由
        next()
      &#125; else &#123;
        try &#123;
          // 获取用户信息
          await store.dispatch('user/getInfo')

          // 重点在这。。。。
          // 根据角色生成路由表
          const accessRoutes = await store.dispatch('permission/generateRoutes')
          // 动态添加路由
          router.addRoutes(accessRoutes)

          next(&#123; ...to, replace: true &#125;)
        &#125; catch (error) &#123;
          console.log(error)
          // 清除token，跳转登录页
          await store.dispatch('user/resetToken')
          Message.error(error || 'Has Error')
          next(`/login?redirect=$&#123;to.path&#125;`)
          NProgress.done()
        &#125;
      &#125;
    &#125;
  &#125; else &#123;

    if (whiteList.indexOf(to.path) !== -1) &#123;
      // 访问的路径处于白名单中
      next()
    &#125; else &#123;
      // 没有登录，跳转登录页
      next(`/login?redirect=$&#123;to.path&#125;`)
      NProgress.done()
    &#125;
  &#125;
&#125;)

router.afterEach(() => &#123;
  NProgress.done()
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个时候基本就好了，因为把路由格式化好的信息放到了Vuex中，菜单组件也可以拿到数据，会自动渲染的。还有一个要补充的地方就是 <code>formatRoutes</code> 函数，这个函数做的事情也很简单，先看代码吧</p>
<pre><code class="copyable">function loadView(component) &#123;
  return (resolve) => require([`@/views/$&#123;component&#125;`], resolve)
&#125;

export default function formatRoutes(routes, Layout) &#123;
  const formatRoutesArr = []
  routes.forEach(route => &#123;
    const router = &#123;
      meta: &#123;&#125;
    &#125;
    const &#123;
      pid,
      title,
      path,
      redirect,
      component,
      keep_alive,
      icon,
      name,
      children
    &#125; = route
    if (component === 'Layout') &#123;
      router['component'] = Layout
    &#125; else &#123;
      router['component'] = loadView(component)
    &#125;
    if (redirect !== null) &#123;
      router['redirect'] = redirect
    &#125;
    if (icon !== null) &#123;
      router['meta']['icon'] = icon
    &#125;
    if (children && children instanceof Array && children.length > 0) &#123;
      router['children'] = formatRoutes(children)
    &#125;
    if (name !== null) &#123;
      router['name'] = name
    &#125;
    router['meta']['title'] = title
    router['path'] = path
    if (pid === 0) &#123;
      router['alwaysShow'] = true
    &#125;
    router['meta']['noCache'] = !keep_alive
    formatRoutesArr.push(router)
  &#125;)
  // 将404页面添加到最后面
  formatRoutesArr.push(&#123; path: '*', redirect: '/404', hidden: true &#125;)
  return formatRoutesArr
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到有很多的if判断语句，其实就是为了完全筛选出我们需要的信息，比如一些为值null的属性，不希望这些属性出现在最后的路由表中，好像只能用这种笨方法了,其实再在forEach嵌一个for循环也差不多，都要判断。<strong>敲黑板</strong>！这里要注意的就是，在导入组件的时候最好不要使用import()导入，会出很多问题的，导入的时候也要多写一层路径，例如千万不要把<code>require(['@/views/$&#123;component&#125;'], resolve)</code>写成<code>require(['@/$&#123;component&#125;'], resolve)</code>因为我最初从数据库拿出来的 <code>component</code> 字段是包含了<code>/view</code>这层路径的，然后一直出错，都要哭了。</p>
<p>走完上面这些流程基本上都能成功，至于说菜单组件怎么渲染数据，这就不是重点了，然后就到了激动人心的时候了，看看效果。</p>
<h2 data-id="heading-5">效果演示</h2>
<p>1.先来看看不同用户登录后台的效果，先来看看超级管理员登录之后的界面</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6168fc52079f4d529128f49e1d1faad0~tplv-k3u1fbpfcp-watermark.image" alt="2.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后我们换一个帐号，这个帐号拥有的角色是发货员和仓库管理员</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3da4fd0258c419699fb8dd2820b4ded~tplv-k3u1fbpfcp-watermark.image" alt="3.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>前面我提到的超级管理员可以控制路由可以被哪些角色访问，也来看看吧，具体实现也很简单。就不再这篇文章中讲了。比如现在超级管理员超级不高兴，不想让发货员访问订单管理这个菜单了，这也是可以的，好吧。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2bc211692f5d4be986245351568249d3~tplv-k3u1fbpfcp-watermark.image" alt="4.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后这个用户登录之后，就会发现没有订单管理这个菜单了</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3d06d7b6888401eade69a8def9da8f7~tplv-k3u1fbpfcp-watermark.image" alt="5.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">最后</h2>
<p>我也是第一次搞这种权限控制，还是前后端一起搞。之前没搞过，也不会，这次也是自己一点点摸索，问题层出不穷，一次一次摔倒又一次次站起来。虽然花了很多的时间，但是最后做出来的时候还是挺有成就感的。我还有太多的东西需要去学习，对自己的要求就是能够坚持下去就好了。</p>
<p>嘿，陌生人。你的点赞或许是对我最大的鼓励！</p></div>  
</div>
            