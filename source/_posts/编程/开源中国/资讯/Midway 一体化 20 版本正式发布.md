
---
title: 'Midway 一体化 2.0 版本正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/79714d40-55e5-4784-b00a-40e3bf5ff6b1.png'
author: 开源中国
comments: false
date: Tue, 24 Aug 2021 13:11:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/79714d40-55e5-4784-b00a-40e3bf5ff6b1.png'
---

<div>   
<div class="content">
                                                                    
                                                        <blockquote> 
 <p>Midway 是一个面向未来的云端一体 Node.js 框架。</p> 
 <p>开源仓库地址：https://github.com/midwayjs/midway，欢迎关注。</p> 
</blockquote> 
<p>在经过近 6 个月的孵化与研发，Midway 一体化 正式发布 2.0 版本，本次更新速览：</p> 
<h2>新功能</h2> 
<h3><strong><strong>运行时升级</strong></strong></h3> 
<p>在 1.0 版本中，我们通过编译器来实现 Hooks 的功能。但这也带来了启动速度慢、语法限制、TS 版本兼容等一系列的问题。</p> 
<p>而在 2.0 版本中，我们移除了原有的编译器实现，通过 Node.js AsyncLocalStorage 来实现对 Hooks 功能的支持。而新版本运行时的实现，不仅移除了之前的诸多问题，同时也解锁了更多的可能性。</p> 
<ul> 
 <li> <h3>减少语法限制</h3> </li> 
</ul> 
<p>在 1.0 中，为了能让编译器正确识别 Hooks，我们要求对 Hooks 的命名、调用、定义均作出了限制。对于开发者而言，命名与使用时都存在一定的负担。</p> 
<p><img src="https://oscimg.oschina.net/oscnet/79714d40-55e5-4784-b00a-40e3bf5ff6b1.png" referrerpolicy="no-referrer"></p> 
<p>而在 2.0 中，得益于运行时的升级，原有的规则与限制均不复存在。你可以在任何函数中使用 Hooks，不受命名的限制。</p> 
<p>如下面的代码，实际上是可以运行的。</p> 
<p><img src="https://oscimg.oschina.net/oscnet/5aa441ac-d12f-4262-81c2-d4bf6baaa864.png" referrerpolicy="no-referrer"></p> 
<p>当然，我们依然推荐在调用 Hooks 的函数使用 use 命名，便于开发者识别到这是一个 Hooks 调用。</p> 
<ul> 
 <li> <h3>代码复用</h3> </li> 
</ul> 
<p>在 1.0 中，由于编译器的限制，Hooks 代码仅能在项目中编写及使用，并不支持发布为 npm 包供其它项目复用。在一定程度上造成了不必要的冗余。</p> 
<p>而在 2.0 中，我们支持了 Hooks 代码复用。你可以像开发任何 npm 包一样，去开发可复用的 Hooks，无需额外的处理，项目中使用时正常导入即可。</p> 
<p>如下图所示，使用第三方的 Hooks 包，加速开发。（图中的包为示例代码，实际并不存在）</p> 
<p><img src="https://oscimg.oschina.net/oscnet/6038d6d8-84fe-435c-a0c7-68dba4f6e64b.png" width="752" referrerpolicy="no-referrer"></p> 
<ul> 
 <li> <h3>极速启动</h3> </li> 
</ul> 
<p>在 1.0 版中，服务启动时存在大量的编译工作，因此新项目首次启动时间 > 10 秒，并随着后端文件的增加，编译时间也会变长，从而导致了项目越大，开发速度越慢的问题。</p> 
<p><img src="https://oscimg.oschina.net/oscnet/db681dca-2195-480f-9125-1755a410934a.png" referrerpolicy="no-referrer"></p> 
<p>1.0 启动流程</p> 
<p>而在 2.0 版本中，得益于纯运行时方案，<strong>新项目启动与重启时间 < 2 秒</strong>，且文件数量的增长并不会影响启动时间。在大型项目中将有效减少等待时间。</p> 
<p>同时，由于不再需要编译器，2.0 版本在运行时也不会产生 .faas_debug_tmp 此类的缓存文件夹，项目目录更加整洁。</p> 
<h3><strong><strong>单元测试</strong></strong></h3> 
<p>单元测试是 Midway Hooks 在函数式支持上的一块重要拼图。我们希望你能轻松愉悦的完成应用的测试，就像测试纯函数那么简单。</p> 
<p>在新版本中，我们支持 runFunction 与 request 两种测试方式，帮助你快速完成接口的测试。</p> 
<p>接口代码</p> 
<pre><code>export async function get () &#123;</code><code>  return &#123; type: 'GET' &#125; </code><code>&#125;</code>
<code>export async function post (message: string) &#123;</code><code>  return &#123; type: 'POST', message &#125;</code><code>&#125;</code></pre> 
<p>使用 runFunction 测试</p> 
<pre><code>import &#123; createApp &#125; from '@midwayjs/hooks-testing-library';</code><code>import &#123; get, post &#125; from './api'</code>
<code>it('GET', async () => &#123;</code><code>  const app = await createApp();</code>
<code>  expect(</code><code>    await app.runFunction(get);</code><code>  ).toEqual(&#123; type: 'GET' &#125;);</code>
<code>  expect(</code><code>    await app.runFunction(post, '2.0');</code><code>  ).toEqual(&#123; type: 'POST', message: '2.0' &#125;);  </code><code>&#125;);</code></pre> 
<p>使用 request 执行完整的 HTTP 测试</p> 
<pre><code>import &#123; createApp &#125; from '@midwayjs/hooks-testing-library';</code><code>import &#123; get, post &#125; from './api'</code>
<code>it('GET', async () => &#123;</code><code>  const app = await createApp();</code>
<code>  const response = await app.request(get)</code><code>  expect(response.status).toEqual(200)</code><code>  expect(response.type).toEqual('application/json')</code>
<code>  const postResponse = await app.request(post, '2.0')</code><code>  expect(postResponse.status).toEqual(200)</code><code>  expect(postResponse.type).toEqual('application/json')</code><code>&#125;);</code></pre> 
<p>对比与传统 Web 应用的测试，你无需关心单元测试的路径、入参、类型提示等。就像测试纯函数一样测试接口。</p> 
<p>传统 Web 应用的测试</p> 
<p><img src="https://oscimg.oschina.net/oscnet/a3995366-e162-45af-b01c-e37cc154401c.png" referrerpolicy="no-referrer"></p> 
<h3><strong><strong>插件化与函数式配置</strong></strong></h3> 
<p>在 1.0 中，我们通过 faas-cli 的插件来为项目启用一体化功能。Midway Hooks 与项目是高度定制化且绑定的。</p> 
<p>而在 2.0 中，我们将 Midway Hooks 变为了 Midway 的 Component，你可以在任何 Midway 新版本中，启用 Hooks 功能，而不受项目类型，部署模式的限制。</p> 
<p>这也意味着，你不仅可以在一体化项目中使用 Hooks，也可以在纯接口开发或 Midway Web 应用开发时使用 Midway Hooks。</p> 
<p>新版本的启用方式</p> 
<pre><code>import &#123; hooks, createConfiguration &#125; from '@midwayjs/hooks';</code>
<code>export default createConfiguration(&#123;</code><code>  imports: [hooks()]</code><code>&#125;);</code></pre> 
<p>同时我们也支持了 createConfiguration，支持以函数的方式创建 Midway Configuration，减少 Class 与函数式混用所带来的迷惑感。</p> 
<h3><strong><strong>Hook 中间件</strong></strong></h3> 
<p>在 1.0 版本中，我们对单函数中间件做了支持，但中间件依然遵照 Koa 中间件的语法，也无法在内部使用 Hooks，会给使用者带来困扰。</p> 
<p>而在 2.0 版本中，我们新增了 Hooks 中间件的支持，同时也支持了全局中间件与文件级中间件。</p> 
<p>原有 1.0 版本的单函数中间件依然保持兼容，你可以手动重构从而使用新的语法。</p> 
<ul> 
 <li> <h4>语法</h4> </li> 
</ul> 
<p>中间件仅有 next 一个参数，ctx 需要通过 useContext 获得。你也可以在中间件中使用任意的 Hooks。</p> 
<p>Logger 中间件</p> 
<pre><code>import &#123; Context &#125; from '@midwayjs/faas';</code><code>import &#123; useContext &#125; from '@midwayjs/hooks';</code>
<code>const logger = async (next: any) => &#123;</code><code>  const ctx = useContext<Context>();</code>
<code>  console.log(`<-- [$&#123;ctx.method&#125;] $&#123;ctx.url&#125;`);</code>
<code>  const start = Date.now();</code><code>  await next();</code><code>  const cost = Date.now() - start;</code>
<code>  console.log(`[$&#123;ctx.method&#125;] $&#123;ctx.url&#125; $&#123;cost&#125;ms`);</code><code>&#125;;</code></pre> 
<p>在 2.0 版本中，Midway Hooks 支持三种形式的中间件，用来覆盖不同的使用诉求。</p> 
<ol> 
 <li> <p>2.0 全局，对所有 Api 调用都生效</p> </li> 
 <li> <p>2.0 文件，对文件内部所有 Api 生效</p> </li> 
 <li> <p>1.0 函数，仅对该 Api 函数生效</p> </li> 
</ol> 
<ul> 
 <li> <h4>全局中间件</h4> </li> 
</ul> 
<p>全局中间件在 configuration.ts 中定义，可以传入任何框架支持的中间件</p> 
<pre><code>import &#123; hooks, createConfiguration &#125; from '@midwayjs/hooks';</code><code>import logger from './logger';</code>
<code>// Global Middleware</code><code>export default createConfiguration(&#123;</code><code>  imports: [</code><code>    hooks(&#123;</code><code>      middleware: [logger],</code><code>    &#125;),</code><code>  ],</code><code>&#125;);</code></pre> 
<ul> 
 <li> <h4>文件级中间件</h4> </li> 
</ul> 
<p>文件级中间件在 Api 文件中定义，通过导出 config.middleware，使得其对该文件内所有 Api 函数生效。</p> 
<pre><code>import &#123; ApiConfig &#125; from '@midwayjs/hooks';</code><code>import logger from './logger';</code>
<code>// File Level Middleware</code><code>export const config: ApiConfig = &#123;</code><code>  middleware: [logger],</code><code>&#125;;</code>
<code>export default async (message: string) => &#123;</code><code>  return &#123; type: 'POST', message &#125;</code><code>&#125;;</code></pre> 
<h3><strong><strong>新配置文件项目配置</strong></strong></h3> 
<p>在 2.0 版本中，我们开放了 Hooks 项目的配置，帮助用户来更好的开发代码。</p> 
<ul> 
 <li> <h4>新配置文件</h4> </li> 
</ul> 
<p>在 1.0 版本中，我们将部分项目的配置存放于 f.yml 中。由于 f.yml 仅适用于 FaaS，且纯文本无法满足用户自定义的诉求。因此，我们在 2.0 版本中推出了新的配置文件：midway.config.ts。</p> 
<p>你可以通过 @midwayjs/hooks 提供的 defineConfig 来配置项目。</p> 
<p>基础配置速览</p> 
<pre><code>import &#123; defineConfig &#125; from '@midwayjs/hooks';</code>
<code>export default defineConfig(&#123;</code><code>  source: 'src/apis',</code><code>  routes: [</code><code>    &#123;</code><code>      baseDir: 'lambda',</code><code>      basePath: '/api',</code><code>    &#125;,</code><code>  ],</code><code>&#125;);</code></pre> 
<p>支持的所有配置</p> 
<pre><code>export interface UserConfig &#123;</code><code>  /**</code><code>   * @default false</code><code>   * Enable superjson to serialize Set/Map/Error/BigInt, default is false</code><code>   */</code><code>  superjson?: boolean</code><code>  // 后端文件夹</code><code>  source?: string</code><code>  // 前端路由</code><code>  routes: ServerRoute[]</code><code>  // devServer 配置</code><code>  dev?: &#123;</code><code>    ignorePattern?: (req: &#123; url: string; [key: string]: any &#125;) => boolean</code><code>  &#125;</code><code>&#125;</code></pre> 
<ul> 
 <li> <h4>文件路由配置</h4> </li> 
</ul> 
<p>在 1.0 中，文件路由在 f.yml 配置。而在 2.0 版本中，文件路由统一在 midway.config.ts 中配置。</p> 
<p>在 2.0 中，我们了开放 Hooks 目录的配置，从而适配不同类型的项目。</p> 
<ol> 
 <li> <p>默认配置：/src/apis</p> </li> 
 <li> <p>自定义：/src/server</p> </li> 
 <li> <p>纯接口项目：/src</p> </li> 
</ol> 
<p>同时我们也大幅度简化了配置的层级，默认支持 HTTP 路由的配置，从而降低开发者的阅读成本。</p> 
<ul> 
 <li> <h4>DevServer 配置</h4> </li> 
</ul> 
<p>在 2.0 中，我们也支持了 devServer 的配置。</p> 
<p>你可以通过传入 dev.ignorePattern 来决定哪些请求应该被 FaaS 函数托管，适用于需要匹配类似 /download/a.css 这种处理文件的情况。</p> 
<p>多场景</p> 
<p>在 2.0 版本中，我们带来了更多场景的支持。</p> 
<h3><strong><strong>纯接口场景</strong></strong></h3> 
<p>在 2.0 中，得益于 Hooks 与 Midway 体系的打通，我们支持了非一体化项目的开发。</p> 
<p>纯接口项目的目录结构</p> 
<p><img src="https://oscimg.oschina.net/oscnet/b8b935e4-680f-4faf-861b-5a176f0c6c55.png" referrerpolicy="no-referrer"></p> 
<p>你可以使用 Hooks 来快速创建接口，并在任何地方调用。而在前后端分离的场景下，我们也在考虑如何为 Hooks 纯接口项目生成前端 SDK 供其它项目使用。</p> 
<h3><strong><strong>Web 场景</strong></strong></h3> 
<p>在 2.0 版本中，我们新增了 Web 服务器部署的支持，这也意味着除了使用 FaaS 平台外，你也可以部署到自己购买的服务器了。</p> 
<p>在 Web 场景下，我们默认使用 Koa 作为底层服务框架，这也意味着你可以使用任何 Koa 中间件来开发应用。</p> 
<p>例子：使用 koa-bodyparser 来解析 body</p> 
<pre><code>import &#123; hooks, createConfiguration &#125; from '@midwayjs/hooks';</code><code>import bodyParser from 'koa-bodyparser';</code>
<code>export default createConfiguration(&#123;</code><code>  imports: [</code><code>    hooks(&#123;</code><code>      // Global Middleware</code><code>      middleware: [bodyParser()],</code><code>    &#125;),</code><code>  ],</code><code>&#125;);</code></pre> 
<p>而在使用上，Web 与 FaaS 的语法是一致的，只是 useContext 传递的上下文变成了 Koa 的 Context。</p> 
<p>你可以自定义 useKoaContext 来确保拿到正确的上下文定义</p> 
<pre><code>import &#123; useContext &#125; from '@midwayjs/hooks';</code><code>import &#123; Context &#125; from '@midwayjs/koa';</code>
<code>function useKoaContext() &#123;</code><code>  return useContext<Context>();</code><code>&#125;</code>
<code>export default async () => &#123;</code><code>  return &#123;</code><code>    message: 'Hello World',</code><code>    method: useKoaContext().method,</code><code>  &#125;;</code><code>&#125;;</code></pre> 
<h2>开源</h2> 
<p>在 2.0 版本中，我们完全基于开源方式去开发。</p> 
<p>同时，我们也在开源社区做了一些大胆的尝试，带来了以下新功能（目前只面向开源社区开放）。</p> 
<h3><strong><strong>Vite</strong></strong></h3> 
<p>在 2.0 中，我们选择 Vite 作为默认支持的前端构建器。</p> 
<p>如图所示，作为一个跨前端框架 + 启动速度极快 + 拥抱未来的前端构建器，它与 Midway Hooks 的理念是相匹配的，能为用户提供更好更快的开发体验。</p> 
<p>Midway Hooks + Vite</p> 
<p><img src="https://oscimg.oschina.net/oscnet/34336401-079d-4035-84e4-5d4173f613b0.png" referrerpolicy="no-referrer"></p> 
<h3><strong><strong>Prisma</strong></strong></h3> 
<p>对于 Midway Hooks 而言，未来很重要的一个方向是建设类型安全的解决方案，而 Prisma 能帮助我们实现这个目标。</p> 
<p>Prisma 是新一代的数据库 ORM，通过 Schema 来生成对应的客户端代码，从而帮助你专注于业务逻辑中。</p> 
<p><img src="https://oscimg.oschina.net/oscnet/3435c987-af45-4b3a-bb69-08354f731ec2.png" referrerpolicy="no-referrer"></p> 
<p>由于数据库客户端是通过 Schema 生成的，因此在生成时就带有类型信息，是可以实现从前后端再到数据库的类型安全解决方案的。</p> 
<p><img src="https://oscimg.oschina.net/oscnet/09b3b545-f2a4-4b5c-96a0-26df468f9684.png" referrerpolicy="no-referrer"></p> 
<p>开源仓库地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmidwayjs%2Fmidway" target="_blank">https://github.com/midwayjs/midway</a></p>
                                        </div>
                                      
</div>
            