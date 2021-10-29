
---
title: 'Paging 3.0 简介 _ MAD Skills'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1029/125158_09UU_4937141.png'
author: 开源中国
comments: false
date: Fri, 29 Oct 2021 12:58:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1029/125158_09UU_4937141.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt height="208" src="https://static.oschina.net/uploads/space/2021/1029/125158_09UU_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p>欢迎阅读 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fmp%2Fappmsgalbum%3F__biz%3DMzk0NDIwMTExNw%3D%3D%26action%3Dgetalbum%26album_id%3D1797733109421948930%26token%3D1293285389%26lang%3Dzh_CN%23wechat_redirect" target="_blank">MAD Skills 系列</a>之 Paging 3.0！在本文中，我将介绍 Paging 3.0 并重点说明如何将其集成至您应用的数据层。如果您更喜欢通过视频了解此内容，请在此处查看:</p> 
<h3><strong>为什么使用 Paging 3.0？</strong></h3> 
<p>向用户展示一列数据是最常见的 UI 模式之一。当您需要加载大量数据时，可以通过分块异步获取 / 显示数据来提升应用性能。这一模式是如此常见，如果有依赖库可以提供促进实现该模式的抽象，将会为开发者带来巨大的便利。这便是 Paging 3.0 致力解决的用例。作为额外的好处，它还让您的应用可以支持无限的数据集合；而如果您的应用通过网络加载数据，它也为支持本地缓存提供了方便。</p> 
<p>如果您正在使用 Paging 2.0，那么 Paging 3.0 也为其前任所包含的功能提供了一系列改进:</p> 
<ul> 
 <li>优先支持 Kotlin 协程和 Flow。</li> 
 <li>支持通过 RxJava Single 或 Guava ListenableFuture 原语进行异步加载。</li> 
 <li>为响应式 UI 设计提供了内建的加载状态和错误信号，包括重试和刷新功能。</li> 
 <li>改进仓库层，包含对于可取消的支持及简化数据源接口。</li> 
 <li>改进表现层、列表分隔符、自定义页面转换以及加载状态头、脚标。</li> 
</ul> 
<p>如需获取更多内容信息，请查阅 Paging 2.0 到 Paging 3.0 的迁移文档:</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.android.google.cn%2Ftopic%2Flibraries%2Farchitecture%2Fpaging%2Fv3-migration" target="_blank">https://developer.android.google.cn/topic/libraries/architecture/paging/v3-migration</a></p> 
<p><strong>置入数据</strong></p> 
<p>在您应用的架构方案中，Paging 3.0 最适合作为从数据层获取数据并通过 ViewModel 在 UI 层传输数据来对其进行转换和呈现的一种方式。在 Paging 3.0 中，我们通过名为 PagingSource 的类型访问您的数据层，该类型定义了如何围绕 PagingConfig 所定义的范围获取和刷新数据。</p> 
<p>PagingSource 和 Map 类似，都需要定义两个泛型类型: 分页的 Key 的类型和加载的数据的类型。举例来说，从基于 Github API 的页面获取 Repo 项目的 PagingSource 的声明，可以定义为:</p> 
<pre><code>
/* Copyright 2020 Google LLC.  
   SPDX-License-Identifier: Apache-2.0 */

class GithubPagingSource(
    …
) : PagingSource<Int, Repo>()</code></pre> 
<p>△ PagingSource 声明</p> 
<p>功能完整的 PagingSource 需要实现两个抽象方法:</p> 
<ol> 
 <li>load()</li> 
 <li>getRefreshKey()</li> 
</ol> 
<h3><strong>load 方法</strong></h3> 
<p>load() 方法正如其名，是由 Paging 库所调用的，用于异步加载要显示的数据的方法。这一方法会在初始加载或者响应用户滑动至边界时调用。load 方法会传入一个 LoadParams 对象，您可以通过它来确定如何触发 load 方法的调用。此对象中包含了有关 load 操作的信息，包括:</p> 
<ul> 
 <li>将要加载的页面的 Key: 如果这是 load 方法第一次被调用 (初始加载)，LoadParams.key 将会是 null。在这种情况下，您必须定义初始页面 Key。</li> 
 <li>加载大小: 请求所要加载的项目的数量。</li> 
</ul> 
<p>load 方法的返回类型是 LoadResult。它可以是:</p> 
<ul> 
 <li>LoadResult.Page: 针对加载成功。</li> 
 <li>LoadResult.Error: 针对加载失败。</li> 
</ul> 
<pre><code>
/* Copyright 2020 Google LLC.  
   SPDX-License-Identifier: Apache-2.0 */   

override suspend fun load(params: LoadParams<Int>): LoadResult<Int, Repo> &#123;
        val position = params.key ?: GITHUB_STARTING_PAGE_INDEX
        val apiQuery = query + IN_QUALIFIER
        return try &#123;
            val response = service.searchRepos(apiQuery, position, params.loadSize)
            val repos = response.items
            val nextKey = if (repos.isEmpty()) &#123;
                null
            &#125; else &#123;
                // 初始加载大小为 3 * NETWORK_PAGE_SIZE
                // 要保证我们在第二次加载时不会去请求重复的项目。
                position + (params.loadSize / NETWORK_PAGE_SIZE)
            &#125;
            LoadResult.Page(
                data = repos,
                prevKey = if (position == GITHUB_STARTING_PAGE_INDEX) null else position - 1,
                nextKey = nextKey
            )
        &#125; catch (exception: IOException) &#123;
            LoadResult.Error(exception)
        &#125; catch (exception: HttpException) &#123;
            LoadResult.Error(exception)
        &#125;
    &#125;</code></pre> 
<p>△ load 方法实现</p> 
<p>注意，默认情况下，初始加载大小为分页大小的三倍。这样可以保证在列表第一次加载时，即使用户稍作滚动，也能看到足够的数据，从而避免触发太多网络请求。这也是在 PagingSource 实现中计算下一个 Key 时所需要考虑的事情。</p> 
<h3><strong>getRefreshKey 方法</strong></h3> 
<p>刷新 Key 用于 PagingSource.load() 方法后续的刷新调用 (第一次调用是初始加载，使用为 Pager 提供的初始 Key)。每当 Paging 库想要加载新的数据来替代当前列表 (例如，下拉刷新或数据库更新、配置变更、进程终止等情况的发生而导致数据失效) 时，便会发生刷新操作。通常，后续刷新调用会想要重新加载以 PagingState.anchorPosition 为中心的数据，而 PagingState.anchorPosition 则代表了最近所访问的索引位置。</p> 
<pre><code>
/* Copyright 2020 Google LLC.  
   SPDX-License-Identifier: Apache-2.0 */

   // 刷新 Key 用于在初始加载的数据失效后下一个 PagingSource 的加载。
    override fun getRefreshKey(state: PagingState<Int, Repo>): Int? &#123;
        // 我们需要获取与最新访问索引最接近页面的前一个 Key（如果上一个 Key 为空，则为下一个 Key）
        // anchorPosition 即为最近访问的索引
        return state.anchorPosition?.let &#123; anchorPosition ->
            state.closestPageToPosition(anchorPosition)?.prevKey?.plus(1)
                ?: state.closestPageToPosition(anchorPosition)?.nextKey?.minus(1)
        &#125;
    &#125;</code></pre> 
<p>△ getRefreshKey 方法实现</p> 
<h3><strong>Pager 对象</strong></h3> 
<p>在定义了 PagingSource 后，我们现在可以创建 Pager 了。Pager 类负责根据 UI 的请求从 PagingSource 中增量拉取数据集合。由于 Pager 需要访问 PagingSource，所以它通常创建在定义 PagingSource 的数据层中。</p> 
<p>构造 Pager 所需的另一个类是 PagingConfig，它定义了控制 Pager 获取数据方式的参数。除了必选的 pageSize 参数外，PagingConfig 还暴露了许多可选参数，您可以通过它们微调 Pager 的行为:</p> 
<pre><code>
/* Copyright 2020 Google LLC.  
   SPDX-License-Identifier: Apache-2.0 */

private const val NETWORK_PAGE_SIZE = 30

class GithubRepository(private val service: GithubService) &#123;

    fun getSearchResultStream(query: String): Flow<PagingData<Repo>> &#123;
        Log.d("GithubRepository", "New query: $query")
        return Pager(
            config = PagingConfig(
                pageSize = NETWORK_PAGE_SIZE,
                enablePlaceholders = false
            ),
            pagingSourceFactory = &#123; GithubPagingSource(service, query) &#125;
        ).flow
    &#125;
&#125;</code></pre> 
<p>△ 创建 Pager</p> 
<p>上面构造 PagingConfig 的代码中所使用参数的简要说明如下:</p> 
<ul> 
 <li>pageSize: 每次要从 PagingSource 加载项目的数量。</li> 
 <li>enablePlaceholders: 是否需要 PagingData 为尚未加载的数据返回 null。</li> 
</ul> 
<p>通常我们会希望 pageSize 足够的大 (至少足够填充界面的可视区域，但最好是这一数量的 2 到 3 倍)，这样 Pager 就不必为了在屏幕上显示足够的内容，而在用户进行滚动操作时一遍又一遍地获取数据了。</p> 
<h3><strong>获取您的数据</strong></h3> 
<p>Pager 所产生的类型是 PagingData，该类型提供了进入其背后 PagingSource 的不同窗口。当用户滚动列表时，PagingData 会持续从 PagingSource 中获取数据以提供内容。如果 PagingSource 失效，Pager 会发出一个新的 PagingData 以确保已经分页的项目与 UI 中显示的内容同步。将 PagingData 视为某个时间节点中 PagingSource 的快照可能会对您的理解有所帮助。</p> 
<p>由于 PagingSource 是在 PagingSource 失效时发生改变的快照，因此 Paging 库提供了多种以流的形式使用 PagingData 的方式:</p> 
<ul> 
 <li>Kotlin Flow 通过 Pager.flow</li> 
 <li>LiveData 通过 Pager.liveData</li> 
 <li>RxJava Flowable 通过 Pager.flowable</li> 
 <li>RxJava Observable 通过 Pager.observable</li> 
</ul> 
<p>PagingData 的流可以在展示分页项目到 UI 前通过 ViewModel 进行操作和转换。</p> 
<h3><strong>后续</strong></h3> 
<p>按照如上步骤，我们已经将 Paging 3.0 集成到了您应用的数据层中！如何在 UI 中消费 PagingData 以及填充我们的仓库列表，敬请关注我们后续的文章。</p> 
<p> </p>
                                        </div>
                                      
</div>
            