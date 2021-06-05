
---
title: 'Angular路由：懒加载、守卫、动态参数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f74049dabc1c4a07bf4f0ece127f9ef8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 04 Jun 2021 16:36:39 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f74049dabc1c4a07bf4f0ece127f9ef8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://devui.design/" target="_blank" rel="nofollow noopener noreferrer">DevUI</a> 是一款面向企业中后台产品的开源前端解决方案，它倡导<code>沉浸</code>、<code>灵活</code>、<code>至简</code>的设计价值观，提倡设计者为真实的需求服务，为多数人的设计，拒绝哗众取宠、取悦眼球的设计。如果你正在开发 <code>ToB</code> 的<code>工具类产品</code>，DevUI 将是一个很不错的选择！</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f74049dabc1c4a07bf4f0ece127f9ef8~tplv-k3u1fbpfcp-watermark.image" alt="Kagol.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">引言</h1>
<p>路由是将URL请求映射到具体代码的一种机制，在网站的模块划分、信息架构中扮演了重要的角色，而Angular的路由能力非常强大，我们一起来看看吧。</p>
<h1 data-id="heading-1">路由懒加载</h1>
<p>Angular可以根据路由，动态加载相应的模块代码，这个功能是性能优化的利器。</p>
<p>为了加快首页的渲染速度，我们可以设计如下的路由，让首页尽量保持简洁、清爽：</p>
<pre><code class="copyable">const routes: Routes = [
  &#123;
    path: '',
    children: [
      &#123;
        path: 'list',
        loadChildren: () => import('./components/list/list.module').then(m => m.ListModule),
      &#125;,
      &#123;
        path: 'detail',
        loadChildren: () => import('./components/detail/detail.module').then(m => m.DetailModule),
      &#125;,
      ...
    ],
  &#125;,
];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首页只有一些简单的静态元素，而其他页面，比如列表、详情、配置等模块都用<code>loadChildren</code>动态加载。</p>
<p>效果如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60318b1dcc7345d385103108a1608ba4~tplv-k3u1fbpfcp-watermark.image" alt="路由懒加载.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中的<code>components-list-list-module-ngfactory.js</code>文件，只有当访问<code>/list</code>路由时才会加载。</p>
<h1 data-id="heading-2">路由守卫</h1>
<p>当我们访问或切换路由时，会加载相应的模块和组件，路由守卫可以理解为在路由加载前后的钩子，最常见的是进入路由的守卫和离开路由的守卫：</p>
<ul>
<li>canActivate 进入守卫</li>
<li>canDeactivate 离开守卫</li>
</ul>
<p>比如我们想在用户进入详情页之前，判断他是否有权限，就可以使用<code>canActivate</code>守卫。</p>
<h2 data-id="heading-3">增加路由守卫</h2>
<pre><code class="copyable">&#123;
  path: 'detail',
  loadChildren: () => import('./components/detail/detail.module').then(m => m.DetailModule),

  // 路由守卫
  canActivate: [AuthGuard],
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">编写守卫逻辑</h2>
<p>使用CLI命令创建路由守卫模块：</p>
<pre><code class="copyable">ng g guard auth
<span class="copy-code-btn">复制代码</span></code></pre>
<p>auth.guard.ts</p>
<pre><code class="copyable">import &#123; Injectable &#125; from '@angular/core';
import &#123; CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, UrlTree &#125; from '@angular/router';
import &#123; Observable &#125; from 'rxjs';
import &#123; DetailService &#125; from './detail.service';

@Injectable(&#123;
  providedIn: 'root'
&#125;)
export class AuthGuard implements CanActivate &#123;
  constructor(
    private detailService: DetailService,
  ) &#123;&#125;

  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree &#123;
    return new Observable(observer => &#123;
      // 鉴权数据从后台接口异步获取
      this.detailService.getDetailAuth().subscribe((hasPermission: boolean) => &#123;
        observer.next(hasPermission);
        observer.complete();
      &#125;);
    &#125;);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">获取权限service</h2>
<p>获取权限的service：</p>
<pre><code class="copyable">ng g s detail
<span class="copy-code-btn">复制代码</span></code></pre>
<p>detail.service.ts</p>
<pre><code class="copyable">import &#123;Injectable&#125; from '@angular/core';
import &#123; HttpClient &#125; from '@angular/common/http';

@Injectable(&#123; providedIn: 'root' &#125;)
export class DetailService &#123;
  constructor(
    private http: HttpClient,
  ) &#123; &#125;

  getDetailAuth(): any &#123;
    return this.http.get('/detail/auth');
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4a75592577f456783988c5db717feb3~tplv-k3u1fbpfcp-watermark.image" alt="路由守卫.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于我们对<code>/detail</code>路由增加了守卫，不管是从别的路由切换到<code>/detail</code>路由，还是直接访问<code>/detail</code>路由，都无法进入该页面。</p>
<h1 data-id="heading-6">动态路由参数</h1>
<p>在路由中带参数有很多中方法：</p>
<ul>
<li>在path中带参数</li>
<li>在queryString中带参数</li>
<li>不通过链接带参数</li>
</ul>
<h2 data-id="heading-7">在path中带参</h2>
<pre><code class="copyable">&#123;
  path: 'user/:id',
  loadChildren: () => import('./components/user/user.module').then(m => m.UserModule),
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">在queryString中带参数</h2>
<p>html传参</p>
<pre><code class="copyable"><a [routerLink]="['/list']" [queryParams]="&#123;id: '1'&#125;">...</a>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ts传参</p>
<pre><code class="copyable">this.router.navigate(['/list'],&#123; queryParams: &#123; id: '1' &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">通过data传递静态参数</h2>
<blockquote>
<p>注意：通过data传递的路由参数只能是静态的</p>
</blockquote>
<pre><code class="copyable">&#123;
  path: 'detail',
  loadChildren: () => import('./components/detail/detail.module').then(m => m.DetailModule),
  
  // 静态参数
  data: &#123;
    title: '详情'
  &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">通过resolve传递动态参数</h2>
<p>data只能传递静态参数，那我想通过路由传递从后台接口获取到的动态参数，该怎么办呢？</p>
<p>答案是通过<code>resolve</code>配置。</p>
<pre><code class="copyable">&#123;
  path: 'detail',
  loadChildren: () => import('./components/detail/detail.module').then(m => m.DetailModule),
  
  // 动态路由参数
  resolve: &#123;
    detail: DetailResolver
  &#125;,
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">创建Resolver</h3>
<p>detail.resolver.ts</p>
<pre><code class="copyable">import &#123; Injectable &#125; from '@angular/core';
import &#123; Resolve, ActivatedRouteSnapshot, RouterStateSnapshot &#125; from '@angular/router';
import &#123; DetailService &#125; from './detail.service';

@Injectable(&#123; providedIn: 'root' &#125;)
export class DetailResolver implements Resolve<any> &#123;

  constructor(private detailService: DetailService) &#123; &#125;

  resolve(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): any &#123;
    return this.detailService.getDetail();
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">在服务中增加获取详情数据的方法</h3>
<p>detail.service.ts</p>
<pre><code class="copyable">import &#123;Injectable&#125; from '@angular/core';
import &#123; HttpClient &#125; from '@angular/common/http';

@Injectable(&#123; providedIn: 'root' &#125;)
export class DetailService &#123;
  constructor(
    private http: HttpClient,
  ) &#123; &#125;

  getDetailAuth(): any &#123;
    return this.http.get('/detail/auth');
  &#125;

  // 增加的
  getDetail(): any &#123;
    return this.http.get('/detail');
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">获取动态参数</h3>
<p>创建组件</p>
<pre><code class="copyable">ng g c detial
<span class="copy-code-btn">复制代码</span></code></pre>
<p>detail.component.ts</p>
<pre><code class="copyable">import &#123; Component, OnInit &#125; from '@angular/core';
import &#123; ActivatedRoute &#125; from '@angular/router';

@Component(&#123;
  selector: 'app-detail',
  templateUrl: './detail.component.html',
  styleUrls: ['./detail.component.scss']
&#125;)
export class DetailComponent implements OnInit &#123;

  constructor(
    private route: ActivatedRoute,
  ) &#123; &#125;

  ngOnInit(): void &#123;
    // 和获取静态参数的方式是一样的
    const detail = this.route.snapshot.data.detail;
    console.log('detail:', detail);
  &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>欢迎加DevUI小助手微信：devui-official，一起讨论Angular技术和前端技术。</p>
<p>欢迎关注我们<a href="https://devui.design/" target="_blank" rel="nofollow noopener noreferrer">DevUI</a>组件库，点亮我们的小星星🌟：</p>
<p><a href="https://github.com/devcloudfe/ng-devui" target="_blank" rel="nofollow noopener noreferrer">github.com/devcloudfe/…</a></p>
<p>也欢迎使用DevUI新发布的<a href="https://devui.design/admin/" target="_blank" rel="nofollow noopener noreferrer">DevUI Admin</a>系统，开箱即用，10分钟搭建一个美观大气的后台管理系统！</p>
<h1 data-id="heading-14">加入我们</h1>
<p>我们是DevUI团队，欢迎来这里和我们一起打造优雅高效的人机设计/研发体系。招聘邮箱：<a href="mailto:muyang2@huawei.com">muyang2@huawei.com</a>。</p>
<p>文/DevUI Kagol</p>
<p>往期文章推荐</p>
<p><a href="https://juejin.cn/post/6968616701709516836" target="_blank">《今天是儿童节，整个贪吃蛇到编辑器里玩儿吧》</a></p>
<p><a href="https://juejin.cn/post/6968104416784171039" target="_blank">《如何将龙插入到编辑器中？》</a></p>
<p><a href="https://juejin.cn/post/6966993945973194765" target="_blank">《Quill富文本编辑器的实践》</a></p>
<p><a href="https://juejin.cn/post/6967931817215131656" target="_blank">《StepsGuide：一个像跟屁虫一样的组件》</a></p>
<p><a href="https://juejin.cn/post/6956155033410863134" target="_blank">《号外号外！DevUI Admin V1.0 发布啦！》</a></p></div>  
</div>
            