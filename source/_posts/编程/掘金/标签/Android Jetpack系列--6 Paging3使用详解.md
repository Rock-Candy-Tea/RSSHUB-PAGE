
---
title: 'Android Jetpack系列--6. Paging3使用详解'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=1623'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 02:03:20 GMT
thumbnail: 'https://picsum.photos/400/300?random=1623'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">定义</h3>
<ul>
<li>Google 推出的一个应用于 Android 平台的分页加载库；</li>
<li>Paging3和之前版本相差很多，完全可以当成一个新库去学习</li>
<li>之前我们使用ListView和RecyclerView实现分页功能并不难，那么为啥需要paging3呢？</li>
<li>它提供了一套非常合理的分页架构，我们只需要按照它提供的架构去编写业务逻辑，就可以轻松实现分页功能;</li>
<li>关联知识点：协程、Flow、MVVM、RecyclerView、DiffUtil</li>
</ul>
<h3 data-id="heading-1">优点</h3>
<ol>
<li>使用内存缓存数据；</li>
<li>内置请求去重，更有效率的显示数据；</li>
<li>RecyclerView自动加载更多</li>
<li>支持Kotlin的协程和Flow，以及LiveData和RxJava2</li>
<li>内置状态处理：刷新，错误，加载等</li>
</ol>
<h3 data-id="heading-2">使用流程如下：</h3>
<h5 data-id="heading-3">需求：</h5>
<ul>
<li>展示GitHub上所有Android相关的开源库，以Star数量排序，每页返回5条数据；</li>
</ul>
<h5 data-id="heading-4">1. 引入依赖</h5>
<pre><code class="copyable">//paging3
implementation 'androidx.paging:paging-runtime-ktx:3.0.0-beta03'
// 用于测试
testImplementation "androidx.paging:paging-common-ktx:3.0.0-beta03"
// [可选] RxJava 支持
implementation "androidx.paging:paging-rxjava2-ktx:3.0.0-beta03"
//retrofit网络请求库
implementation 'com.squareup.retrofit2:retrofit:2.9.0'
implementation 'com.squareup.retrofit2:converter-gson:2.9.0'
//下拉刷新
implementation 'androidx.swiperefreshlayout:swiperefreshlayout:1.1.0'
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-5">2. 创建数据模型类 RepoResponse</h5>
<pre><code class="copyable">class RepoResponse &#123;
    @SerializedName("items") val items:List<Repo> = emptyList()
&#125;
data class Repo(
    @SerializedName("id") val id: Int,
    @SerializedName("name") val name: String,
    @SerializedName("description") val description: String,
    @SerializedName("stargazers_count") val starCount: String,
)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-6">3. 定义网络请求接口 ApiService</h5>
<pre><code class="copyable">interface ApiService &#123;
    @GET("search/repositories?sort=stars&q=Android")
    suspend fun searRepos(@Query("page") page: Int, @Query("per_page") perPage: Int): RepoResponse

    companion object &#123;
        private const val BASE_URL = "https://api.github.com/"
        fun create(): ApiService &#123;
            return Retrofit.Builder()
                .baseUrl(BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .build()
                .create(ApiService::class.java)
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">4. 配置数据源</h5>
<ul>
<li>自定义一个子类继承PagingSource，然后重写 load() 函数，并在这里提供对应当前页数的数据, 这一步才真正用到了Paging3</li>
<li>PagingSource的两个泛型参数，一个是页数类型，一个是数据item类型</li>
</ul>
<pre><code class="copyable">class RepoPagingSource(private val apiService: ApiService) : PagingSource<Int, Repo>() &#123;
    override fun getRefreshKey(state: PagingState<Int, Repo>): Int? &#123;
        return null
    &#125;

    override suspend fun load(params: LoadParams<Int>): LoadResult<Int, Repo> &#123;
        return try &#123;
            val page = params.key ?: 1
            val pageSize = params.loadSize
            val repoResponse = apiService.searRepos(page, pageSize)
            val repoItems = repoResponse.items
            val prevKey = if (page > 1) page - 1 else null
            val nextKey = if (repoItems.isNotEmpty()) page + 1 else null
            LoadResult.Page(repoItems, prevKey, nextKey)
        &#125; catch (e: Exception) &#123;
            LoadResult.Error(e)
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-8">5. 在ViewModel中实现接口请求</h5>
<ul>
<li>PagingConfig的一个参数prefetchDistance，用于表示距离底部多少条数据开始预加载，设置0则表示滑到底部才加载，默认值为分页大小；若要让用户对加载无感，适当增加预取阈值即可，比如调整到分页大小的5倍；</li>
<li>cachedIn() 是 Flow 的扩展方法，用于将服务器返回的数据在viewModelScope这个作用域内进行缓存，假如手机横竖屏发生了旋转导致Activity重新创建，Paging 3就可以直接读取缓存中的数据，而不用重新发起网络请求了。</li>
</ul>
<pre><code class="copyable">//1. Repository中实现网络请求
object Repository &#123;
    private const val PAGE_SIZE = 5
    private val gitHubService = ApiService.create()
    fun getPagingData(): Flow<PagingData<Repo>> &#123;
        // PagingConfig的一个参数prefetchDistance，用于表示距离底部多少条数据开始预加载，
        // 设置0则表示滑到底部才加载。默认值为分页大小。
        // 若要让用户对加载无感，适当增加预取阈值即可。 比如调整到分页大小的5倍
        return Pager(config = PagingConfig(pageSize = PAGE_SIZE, prefetchDistance = PAGE_SIZE * 5),
            pagingSourceFactory = &#123; RepoPagingSource(gitHubService) &#125;).flow
    &#125;
&#125;
//2. ViewModel中调用Repository
class Paging3ViewModel : ViewModel() &#123;
    fun getPagingData(): Flow<PagingData<Repo>> &#123;
        return Repository.getPagingData().cachedIn(viewModelScope)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-9">6. 实现RecyclerView的Adapter</h5>
<ul>
<li>必须继承 PagingDataAdapter</li>
</ul>
<pre><code class="copyable">class RepoAdapter : PagingDataAdapter<Repo, RepoAdapter.ViewHolder>(COMPARATOR) &#123;
    companion object &#123;
        //因为Paging 3在内部会使用DiffUtil来管理数据变化，所以这个COMPARATOR是必须的
        private val COMPARATOR = object : DiffUtil.ItemCallback<Repo>() &#123;
            override fun areItemsTheSame(oldItem: Repo, newItem: Repo): Boolean &#123;
                return oldItem.id == newItem.id
            &#125;

            override fun areContentsTheSame(oldItem: Repo, newItem: Repo): Boolean &#123;
                return oldItem == newItem
            &#125;
        &#125;
    &#125;

    class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView)&#123;
        val binding: LayoutRepoItemBinding? =DataBindingUtil.bind(itemView)
    &#125;

    override fun onBindViewHolder(holder: ViewHolder, position: Int) &#123;
        holder.binding?.repo=getItem(position)
    &#125;

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder &#123;
        val view=LayoutInflater.from(parent.context).inflate(R.layout.layout_repo_item,parent,false)
        return ViewHolder(view)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-10">7. FooterAdapter的实现</h5>
<ul>
<li>用于实现加载更多，必须继承自LoadStateAdapter，</li>
<li>retry():使用Kotlin的高阶函数来给重试按钮注册点击事件</li>
</ul>
<pre><code class="copyable">class FooterAdapter(val retry: () -> Unit) : LoadStateAdapter<FooterAdapter.ViewHolder>() &#123;
    class ViewHolder(val binding: ViewDataBinding) : RecyclerView.ViewHolder(binding.root)

    override fun onBindViewHolder(holder: ViewHolder, loadState: LoadState) &#123;
        val binding=holder.binding as LayoutFooterItemBinding
        when (loadState) &#123;
            is LoadState.Error -> &#123;
                binding.progressBar.visibility = View.GONE
                binding.retryButton.visibility = View.VISIBLE
                binding.retryButton.text = "Load Failed, Tap Retry"
                binding.retryButton.setOnClickListener &#123;
                    retry()
                &#125;
            &#125;
            is LoadState.Loading -> &#123;
                binding.progressBar.visibility = View.VISIBLE
                binding.retryButton.visibility = View.VISIBLE
                binding.retryButton.text = "Loading"
            &#125;
            is LoadState.NotLoading -> &#123;
                binding.progressBar.visibility = View.GONE
                binding.retryButton.visibility = View.GONE
            &#125;
        &#125;
    &#125;

    override fun onCreateViewHolder(parent: ViewGroup, loadState: LoadState): ViewHolder &#123;
        val binding: LayoutFooterItemBinding =
            LayoutFooterItemBinding.inflate(
                LayoutInflater.from(parent.context), parent, false
            )
        return ViewHolder(binding)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-11">8. 在Activity中使用</h5>
<ul>
<li>mAdapter.submitData()是触发Paging 3分页功能的核心; 它接收一个PagingData参数，这个参数我们需要调用ViewModel中返回的Flow对象的collect()函数才能获取到，collect()函数有点类似于Rxjava中的subscribe()函数，总之就是订阅了之后，消息就会源源不断往这里传。不过由于collect()函数是一个挂起函数，只有在协程作用域中才能调用它，因此这里又调用了lifecycleScope.launch()函数来启动一个协程。</li>
<li>加载更多：通过mAdapter.withLoadStateFooter实现;</li>
<li>下拉刷新：这里下来刷新是配合SwipeRefreshLayout使用，在其OnRefreshListener中调用mAdapter.refresh(),并在mAdapter.addLoadStateListener中处理下拉刷新的UI逻辑；</li>
<li>虽然有withLoadStateHeader，但它并不是用于实现刷新，而是加载上一页，需要当前起始页>1时才生效</li>
</ul>
<pre><code class="copyable">class Paging3Activity : AppCompatActivity() &#123;
    private val viewModel by lazy &#123;
        ViewModelProvider(this).get(Paging3ViewModel::class.java)
    &#125;
    private val mAdapter:RepoAdapter = RepoAdapter()

    override fun onCreate(savedInstanceState: Bundle?) &#123;
        super.onCreate(savedInstanceState)
        //在Activity中使用
        val binding: ActivityPaging3Binding =
            DataBindingUtil.setContentView(this, R.layout.activity_paging3)
        binding.lifecycleOwner = this
        //下拉刷新
        binding.refreshlayout.setOnRefreshListener &#123;
            mAdapter.refresh()
        &#125;
        binding.recyclerView.layoutManager = LinearLayoutManager(this)
        //添加footer
        binding.recyclerView.adapter = mAdapter.withLoadStateFooter(FooterAdapter &#123;
            mAdapter.retry()
        &#125;)
//        binding.recyclerView.adapter = repoAdapter.withLoadStateHeaderAndFooter(
//            header = HeaderAdapter &#123; repoAdapter.retry() &#125;,
//            footer = FooterAdapter &#123; repoAdapter.retry() &#125;
//        )
        lifecycleScope.launch &#123;
            viewModel.getPagingData().collect &#123;
                mAdapter.submitData(it)
            &#125;
        &#125;
        //监听加载状态
        mAdapter.addLoadStateListener &#123;
            //比如处理下拉刷新逻辑
            when (it.refresh) &#123;
                is LoadState.NotLoading -> &#123;
                    binding.recyclerView.visibility = View.VISIBLE
                    binding.refreshlayout.isRefreshing = false
                &#125;
                is LoadState.Loading -> &#123;
                    binding.refreshlayout.isRefreshing = true
                    binding.recyclerView.visibility = View.VISIBLE
                &#125;
                is LoadState.Error -> &#123;
                    val state = it.refresh as LoadState.Error
                    binding.refreshlayout.isRefreshing = false
                    Toast.makeText(this, "Load Error: $&#123;state.error.message&#125;", Toast.LENGTH_SHORT)
                        .show()
                &#125;
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-12">9. RemoteMediator</h5>
<h6 data-id="heading-13">RemoteMediator 和 PagingSource 的区别：</h6>
<ul>
<li>PagingSource：实现单一数据源以及如何从该数据源中查找数据，推荐用于加载有限的数据集（本地数据库），例如 Room，数据源的变动会直接映射到 UI 上；</li>
<li>RemoteMediator：实现加载网络分页数据并更新到数据库中，但是数据源的变动不能直接映射到 UI 上；</li>
<li>可以使用 RemoteMediator 实现从网络加载分页数据更新到数据库中，使用 PagingSource 从数据库中查找数据并显示在 UI 上</li>
</ul>
<h6 data-id="heading-14">RemoteMediator的使用</h6>
<ol>
<li>定义数据源</li>
</ol>
<pre><code class="copyable">// 本地数据库存储使用的Room，Room使用相关的之后会在另一篇文章中详细介绍，这里直接贴代码了
//1. 定义实体类，并添加@Entity注释
@Entity
data class RepoEntity(
    @PrimaryKey  val id: Int,
    @ColumnInfo(name = "name")  val name: String,
    @ColumnInfo(name = "description") val description: String,
    @ColumnInfo(name = "star_count")  val starCount: String,
    @ColumnInfo(name = "page") val page: Int ,
)

//2. 定义数据访问对象RepoDao
@Dao
interface RepoDao &#123;
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insert(pokemonList: List<RepoEntity>)

    @Query("SELECT * FROM RepoEntity")
    fun get(): PagingSource<Int, RepoEntity>

    @Query("DELETE FROM RepoEntity")
    suspend fun clear()

    @Delete
    fun delete(repo: RepoEntity)

    @Update
    fun update(repo: RepoEntity)
&#125;

//3. 定义Database
@Database(entities = [RepoEntity::class], version = Constants.DB_VERSION)
abstract class AppDatabase : RoomDatabase() &#123;
    abstract fun repoDao(): RepoDao

    companion object &#123;
        val instance = AppDatabaseHolder.db
    &#125;

    private object AppDatabaseHolder &#123;
        val db: AppDatabase = Room
            .databaseBuilder(
                AppHelper.mContext,
                AppDatabase::class.java,
                Constants.DB_NAME
            )
            .allowMainThreadQueries() //允许在主线程中查询
            .build()
    &#125;
&#125;

//4. 数据库常量管理
interface Constants &#123;
    /**
     * 数据库名称
     */
    String DB_NAME = "JetpackDemoDataBase.db";

    /**
     * 数据库版本
     */
    int DB_VERSION = 1;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>实现 RemoteMediator</li>
</ol>
<pre><code class="copyable">// 1. RemoteMediator 目前是实验性的 API ，所有实现 RemoteMediator 的类
//都需要添加 @OptIn(ExperimentalPagingApi::class) 注解,
//使用 OptIn 注解，要App的build.gradle中配置
android &#123;
    kotlinOptions &#123;
        freeCompilerArgs += ["-Xopt-in=kotlin.RequiresOptIn"]
    &#125;
&#125;

//2. 自定义RepoMediator，继承RemoteMediator
//RemoteMediator 和 PagingSource 相似，都需要覆盖 load() 方法，但是其参数不同
@OptIn(ExperimentalPagingApi::class)
class RepoMediator(
    val api: ApiService,
    val db: AppDatabase
) : RemoteMediator<Int, RepoEntity>() &#123;
    override suspend fun load(
        loadType: LoadType,
        state: PagingState<Int, RepoEntity>
    ): MediatorResult &#123;
        val repoDao = db.repoDao()
        val pageKey = when (loadType) &#123;
            //首次访问 或者调用 PagingDataAdapter.refresh()时
            LoadType.REFRESH -> null
            //在当前加载的数据集的开头加载数据时
            LoadType.PREPEND -> return MediatorResult.Success(endOfPaginationReached = true)
            //下拉加载更多时
            LoadType.APPEND -> &#123;
                val lastItem = state.lastItemOrNull()
                if (lastItem == null) &#123;
                    return MediatorResult.Success(
                        endOfPaginationReached = true
                    )
                &#125;
                lastItem.page
            &#125;
        &#125;

        //无网络则加载本地数据
        if (!AppHelper.mContext.isConnectedNetwork()) &#123;
            return MediatorResult.Success(endOfPaginationReached = true)
        &#125;

        //请求网络分页数据
        val page = pageKey ?: 0
        val pageSize = Repository.PAGE_SIZE
        val result = api.searRepos(page, pageSize).items
        val endOfPaginationReached = result.isEmpty()
        val items = result.map &#123;
            RepoEntity(
                id = it.id,
                name = it.name,
                description = it.description,
                starCount = it.starCount,
                page=page + 1
            )
        &#125;

        //插入数据库
        db.withTransaction &#123;
            if (loadType==LoadType.REFRESH)&#123;
                repoDao.clear()
            &#125;
            repoDao.insert(items)
        &#125;
        return MediatorResult.Success(endOfPaginationReached = endOfPaginationReached)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>在 Repository 中构建 Pager</li>
</ol>
<pre><code class="copyable">object Repository &#123;
    const val PAGE_SIZE = 5
    private val gitHubService = ApiService.create()
    private val db = AppDatabase.instance
    private val pagingConfig = PagingConfig(
        // 每页显示的数据的大小
        pageSize = PAGE_SIZE,
        // 开启占位符
        enablePlaceholders = true,
        // 预刷新的距离，距离最后一个 item 多远时加载数据
        // 默认为 pageSize
        prefetchDistance = PAGE_SIZE,
        // 初始化加载数量，默认为 pageSize * 3
        initialLoadSize = PAGE_SIZE
    )

    @OptIn(ExperimentalPagingApi::class)
    fun getPagingData2(): Flow<PagingData<Repo>> &#123;
        return Pager(
            config = pagingConfig,
            remoteMediator = RepoMediator(gitHubService, db)
        ) &#123;
            db.repoDao().get()
        &#125;.flow.map &#123; pagingData ->
            pagingData.map &#123; RepoEntity2RepoMapper().map(it) &#125;
        &#125;
    &#125;
&#125;

class RepoEntity2RepoMapper : Mapper<RepoEntity, Repo> &#123;
    override fun map(input: RepoEntity): Repo = Repo(
        id = input.id,
        name = input.name,
        description = input.description,
        starCount = input.starCount
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>在 ViewModel 获取数据</li>
</ol>
<pre><code class="copyable">class Paging3ViewModel : ViewModel() &#123;
    fun getPagingData2(): LiveData<PagingData<Repo>> =
        Repository.getPagingData2().cachedIn(viewModelScope).asLiveData()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>在Activity中注册观察者</li>
</ol>
<pre><code class="copyable"> viewModel.getPagingData2().observe(this, &#123;
            mAdapter.submitData(lifecycle, it)
        &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>到此打完收工，跑一下代码，发现无网络情况下就会加载数据库中的数据，有网络就会从网络请求数据更新数据库并刷新UI界面</li>
</ul>
<h2 data-id="heading-15">我是今阳，如果想要进阶和了解更多的干货，欢迎关注微信公众号 “今阳说” 接收我的最新文章</h2></div>  
</div>
            