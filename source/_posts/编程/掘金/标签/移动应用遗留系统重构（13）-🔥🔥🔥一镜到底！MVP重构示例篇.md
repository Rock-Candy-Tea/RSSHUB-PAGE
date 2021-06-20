
---
title: '移动应用遗留系统重构（13）-🔥🔥🔥一镜到底！MVP重构示例篇'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a3b64237ff544bf9b01d0d222bba3e3~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 20 Jun 2021 06:06:19 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a3b64237ff544bf9b01d0d222bba3e3~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>上一篇<a href="https://juejin.cn/post/6974634615537401886" target="_blank">移动应用遗留系统重构（12）- 编译调试篇</a>
介绍，经过了解耦、分库及编译调试的优化，一段时间内，CloudDisk的开发效率得到了很大的提升。</p>
<p>但随着业务的演进，由于历史的原因，代码中存在很多Activity及Controller的上帝类。今天我们将拿File Bundle作为例子，为大家总结重构的流程，演示如何一步一步将上帝类重构为MVP架构。</p>
<p><strong>视频演示地址:</strong> <a href="https://mp.weixin.qq.com/s/zjeln_eqAN45CDbSrWjLaA" target="_blank" rel="nofollow noopener noreferrer">mp.weixin.qq.com/s/zjeln_eqA…</a></p>
<h1 data-id="heading-1">重构流程</h1>
<pre><code class="hljs language-mermaid" lang="mermaid">graph TD
A(1.梳理业务逻辑)-->B(2.分析原有的代码设计)
B-->C(3.补充守护测试)
C-->D(4.简单设计)
D-->E(5.小步安全重构)
E-->F(6.集成验收测试)
</code></pre>
<h2 data-id="heading-2">1. 梳理业务逻辑</h2>
<p>通过往往这一步是最难的。由于人员更迭、产品的迭代，给这一步带来很大的挑战。我们可以尝试从一下几方面来补全信息。</p>
<ol>
<li>找人：产品经理、设计人员、测试人员进行确认和答疑</li>
<li>找文档：查看原有的需求文档、设计文档、测试用例、设计稿</li>
<li>看代码：从原有的代码设计中去梳理业务</li>
</ol>
<p>经过梳理确认，File Bundle的现有的业务如下：</p>
<pre><code class="hljs language-mermaid" lang="mermaid">graph TD
A(进入文件页面)-->B(从网络加载文件列表数据)
B --> C&#123;数据是否加载成功&#125;
C -->|加载成功| D(显示文件列表-文件名和文件大小)
C -->|网络异常| E(显示NetworkErrorException)
C -->|数据为空| F(显示empty data)
E -->|点击触发刷新|B
F -->|点击触发刷新|B
</code></pre>
<blockquote>
<p>文件大小转换为以B、K、M、G单位显示</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a3b64237ff544bf9b01d0d222bba3e3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">2.分析原有的代码设计</h2>
<p>我们以主要上帝类FileFragment为例，代码如下：</p>
<pre><code class="copyable">@AndroidEntryPoint
public class FileFragment extends Fragment &#123;

    @Inject
    FileController fileController;

    private RecyclerView fileListRecycleView;
    private TextView tvMessage;

    public static FileFragment newInstance() &#123;
        FileFragment fragment = new FileFragment();
        Bundle args = new Bundle();
        fragment.setArguments(args);
        return fragment;
    &#125;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) &#123;

        View view = inflater.inflate(R.layout.fragment_file, container, false);
        fileListRecycleView = view.findViewById(R.id.file_list);
        tvMessage = view.findViewById(R.id.tv_message);
        tvMessage.setOnClickListener(v -> getFileList());
        return view;
    &#125;

    @Override
    public void onCreate(Bundle savedInstanceState) &#123;
        super.onCreate(savedInstanceState);
        getFileList();
    &#125;

    private void getFileList() &#123;
        new Thread(() -> &#123;
            Message message = new Message();
            try &#123;
                List<FileInfo> infoList = fileController.getFileList();
                message.what = 1;
                message.obj = infoList;
            &#125; catch (NetworkErrorException e) &#123;
                message.what = 0;
                message.obj = "NetworkErrorException";
                e.printStackTrace();
            &#125;
            mHandler.sendMessage(message);
        &#125;).start();
    &#125;

    Handler mHandler = new Handler(new Handler.Callback() &#123;
        @Override
        public boolean handleMessage(@NonNull Message msg) &#123;
            if (msg.what == 1) &#123;
                showTip(false);
                //显示网络数据
                List<FileInfo> infoList = (List<FileInfo>) msg.obj;
                FileListAdapter fileListAdapter = new FileListAdapter(infoList, getActivity());
                fileListRecycleView.addItemDecoration(new DividerItemDecoration(
                        getActivity(), DividerItemDecoration.VERTICAL));
                //设置布局显示格式
                fileListRecycleView.setLayoutManager(new LinearLayoutManager(getActivity()));
                fileListRecycleView.setAdapter(fileListAdapter);
            &#125; else if (msg.what == 0) &#123;
                showTip(true);
                //显示异常提醒数据
                tvMessage.setText(msg.obj.toString());
            &#125; else &#123;
                showTip(true);
                //显示空数据
                tvMessage.setText("empty data");
            &#125;
            return false;
        &#125;
    &#125;);

    public void showTip(boolean show) &#123;
        if (show) &#123;
            tvMessage.setVisibility(View.VISIBLE);
            fileListRecycleView.setVisibility(View.GONE);
        &#125; else &#123;
            tvMessage.setVisibility(View.GONE);
            fileListRecycleView.setVisibility(View.VISIBLE);
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从代码中我们可以看到主要的一些设计问题，如下：</p>
<ol>
<li>主要的获取文件、异常逻辑判断、界面刷新控制都是在一个类里面，不利于后续的扩张及修改维护。我们希望类的职责更加单一，逻辑和视图能够进行分离。</li>
<li>存在粗暴的new Thread进行管理</li>
<li>Handler 存在内存泄露风险</li>
<li>存在规范问题，例如empty data字符串没有使用xml进行管理、代码中由无效的导包等</li>
<li>代码中没有任何守护测试</li>
</ol>
<p>完整的所有代码见<a href="https://github.com/junbin1011/CloudDisk/commit/3c4c4d98bcef46357f4c653431dc53e6d691e397" target="_blank" rel="nofollow noopener noreferrer">Github</a></p>
<h2 data-id="heading-4">3. 补充守护测试</h2>
<p>参考重构篇中，我们制定的策略，我们可以先做大型的测试，做为守护测试。</p>
<pre><code class="copyable">@RunWith(AndroidJUnit4.class)
@LargeTest
@HiltAndroidTest
@Config(application = HiltTestApplication.class)
public class FileFragmentTest &#123;

    @Rule
    public HiltAndroidRule hiltRule = new HiltAndroidRule(this);

    @Test
    public void show_show_file_list_when_get_success() &#123;
        //given
        ActivityScenario<DebugActivity> scenario = ActivityScenario.launch(DebugActivity.class);
        scenario.onActivity(activity -> &#123;
            //then
            onView(withText("遗留代码重构.pdf")).check(matches(isDisplayed()));
            onView(withText("100.00K")).check(matches(isDisplayed()));
            onView(withText("系统组件化.pdf")).check(matches(isDisplayed()));
            onView(withText("9.67K")).check(matches(isDisplayed()));
        &#125;);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>我们发现这个用不会通过，我们主要面临一下2个问题。</strong></p>
<ol>
<li>网络请求是异步的，异步逻辑可能在测试执行完还没有触发到</li>
<li>网络数据是动态的，我们断言的数据没办法确定</li>
</ol>
<p>所以我们采用的做法就是Mock，我不稳定的依赖Mock掉。我们同样使用Shadow来进行多获取网络数据方法进行Mock，代码如下：</p>
<pre><code class="copyable">@Implements(FileFragment.class)
public class ShadowFileFragment &#123;

    @RealObject
    public FileFragment fileFragment;

    enum State &#123;
        SUCCESS,
        ERROR,
        EMPTY
    &#125;

    public static State state = State.SUCCESS;

    @Implementation
    protected void getFileList() &#123;
        System.out.println("shadow .... .....");
        Message message = new Message();
        if (state == State.SUCCESS) &#123;
            ArrayList<FileInfo> infoList = new ArrayList<>();
            infoList.add(new FileInfo("遗留代码重构.pdf", 102400));
            infoList.add(new FileInfo("系统组件化.pdf", 9900));
            message.what = 1;
            message.obj = infoList;
        &#125; else if (state == State.ERROR) &#123;
            message.what = 0;
            message.obj = "NetworkErrorException";
        &#125; else if (state == State.EMPTY) &#123;
            message.what = 1;
            message.obj = null;
        &#125;
        fileFragment.mHandler.sendMessage(message);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调整后的测试用例如下：</p>
<pre><code class="copyable"> @Test
    public void show_show_file_list_when_get_success() &#123;
        //given
        ShadowFileFragment.state = ShadowFileFragment.State.SUCCESS;
        //when
        ActivityScenario<DebugActivity> scenario = ActivityScenario.launch(DebugActivity.class);
        scenario.onActivity(activity -> &#123;
            //then
            onView(withText("遗留代码重构.pdf")).check(matches(isDisplayed()));
            onView(withText("100.00K")).check(matches(isDisplayed()));
            onView(withText("系统组件化.pdf")).check(matches(isDisplayed()));
            onView(withText("9.67K")).check(matches(isDisplayed()));
        &#125;);
    &#125;

    @Test
    public void show_show_error_tip_when_net_work_exception() &#123;
        //given
        ShadowFileFragment.state = ShadowFileFragment.State.ERROR;
        //when
        ActivityScenario<DebugActivity> scenario = ActivityScenario.launch(DebugActivity.class);
        scenario.onActivity(activity -> &#123;
            //then
            onView(withText("NetworkErrorException")).check(matches(isDisplayed()));
        &#125;);
    &#125;

    @Test
    public void show_show_empty_tip_when_not_has_data() &#123;
        //given
        ShadowFileFragment.state = ShadowFileFragment.State.EMPTY;
        //when
        ActivityScenario<DebugActivity> scenario = ActivityScenario.launch(DebugActivity.class);
        scenario.onActivity(activity -> &#123;
            //then
            onView(withText("empty data")).check(matches(isDisplayed()));
        &#125;);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>中间我们用允许测试脚步时发现，之前的旧代码还有一处逻辑的错误。数据为空的判断应该加在网络数据回调中。</p>
<pre><code class="copyable">Caused by: java.lang.NullPointerException
at com.cloud.disk.bundle.file.FileFragment$1.handleMessage(FileFragment.java:96)
at android.os.Handler.dispatchMessage(Handler.java:102)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们同步将异常逻辑进行修改，如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/035a8a19ed9347289437f5416caa5297~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后我们完成了基本的守护测试，运行结果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ada7610b565544a8ab7cf854945e146c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>完整的所有代码见<a href="https://github.com/junbin1011/CloudDisk/commit/3c4c4d98bcef46357f4c653431dc53e6d691e397" target="_blank" rel="nofollow noopener noreferrer">Github</a></p>
<h2 data-id="heading-5">4. 简单设计</h2>
<h3 data-id="heading-6">MVP架构</h3>
<pre><code class="hljs language-mermaid" lang="mermaid">graph TD
B(Presenter)-->A(Model)
B-->|interface|C(View)
C-->|interface|B
</code></pre>
<ol>
<li>业务逻辑和视图分离</li>
<li>Presenter和View之间通过接口交互</li>
<li>为了更高效管理线程，团队决定使用Rxjava进行线程统一管理。架构风格参考<a href="https://github.com/android/architecture-samples" target="_blank" rel="nofollow noopener noreferrer">architecture-samples</a></li>
</ol>
<h3 data-id="heading-7">接口设计</h3>
<ol>
<li>Contract接口设计</li>
</ol>
<pre><code class="copyable">public interface FileListContract &#123;

    interface View  &#123;
        showFileList(List<FileInfo> fileList);
        showNetWorkException(String errorMessage);
        showEmptyData();
    &#125;

    interface Presenter &#123;

        void getFileList();
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>数据接口设计</li>
</ol>
<pre><code class="copyable">public interface FileDataSource &#123;
     Flowable<List<FileInfo>> getFileList();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">5.小步安全重构</h2>
<ul>
<li>抽取FileFragment的业务逻辑到FilePresenter</li>
<li>FileFragment 提取UI接口</li>
<li>抽取FileDataSource</li>
</ul>
<blockquote>
<p>重构手法包含提取接口、移动方法、移动类、抽取方法、内联、提取变量等等。<strong>过程还需要根据重构适当调整测试用例。</strong></p>
</blockquote>
<p>详细的演示见<a href="https://mp.weixin.qq.com/s/zjeln_eqAN45CDbSrWjLaA" target="_blank" rel="nofollow noopener noreferrer">视频</a></p>
<ul>
<li>补充测试用例</li>
</ul>
<ol>
<li>补充FileUtils计算文件大小测试</li>
</ol>
<pre><code class="copyable">@RunWith(JUnit4.class)
@SmallTest
public class FileUtilsTest &#123;

    @Test
    public void should_return_B_unit_when_file_size_in_its_range() &#123;
        //given
        long fileSize = 100;
        //when
        String format = FileUtils.formatFileSize(fileSize);
        //then
        assertEquals("100.00B", format);
    &#125;

    @Test
    public void should_return_K_unit_when_file_size_in_its_range() &#123;
        //given
        long fileSize = 1034;
        //when
        String format = FileUtils.formatFileSize(fileSize);
        //then
        assertEquals("1.01K", format);
    &#125;

    @Test
    public void should_return_M_unit_when_file_size_in_its_range() &#123;
        //given
        long fileSize = 1084000;
        //when
        String format = FileUtils.formatFileSize(fileSize);
        //then
        assertEquals("1.03M", format);
    &#125;

    @Test
    public void should_return_G_unit_when_file_size_in_its_range() &#123;
        //given
        long fileSize = 1114000000;
        //when
        String format = FileUtils.formatFileSize(fileSize);
        //then
        assertEquals("1.04G", format);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>补充Presenter业务逻辑测试</li>
</ol>
<pre><code class="copyable">@RunWith(JUnit4.class)
@MediumTest
public class FilePresenterImplTest &#123;

    @Rule
    public RxSchedulerRule rule = new RxSchedulerRule();

    @Test
    public void should_return_file_list_when_call_data_source_success() throws NetworkErrorException &#123;
        //given
        FileListContract.View mockView = mock(FileListContract.View.class);
        FileDataSource mockFileDataSource = mock(FileDataSource.class);
        List<FileInfo> fileList = new ArrayList<>();
        fileList.add(new FileInfo("遗留代码重构.pdf", 102400));
        fileList.add(new FileInfo("系统组件化.pdf", 9900));
        when(mockFileDataSource.getFileList()).thenReturn(Flowable.fromArray(fileList));
        FileListContract.FilePresenter filePresenter = new FilePresenterImpl(mockFileDataSource, mockView);
        //when
        filePresenter.getFileList();
        //then
        verify(mockView).showFileList(anyList());
    &#125;

    @Test
    public void should_show_empty_data_when_call_data_source_return_empty() throws NetworkErrorException &#123;
        //given
        FileListContract.View mockView = mock(FileListContract.View.class);
        FileDataSource mockFileDataSource = mock(FileDataSource.class);
        when(mockFileDataSource.getFileList()).thenReturn(Flowable.fromArray(new ArrayList<>()));
        FileListContract.FilePresenter filePresenter = new FilePresenterImpl(mockFileDataSource, mockView);
        //when
        filePresenter.getFileList();
        //then
        verify(mockView).showEmptyData();
    &#125;

    @Test
    public void should_show_network_exception_when_call_data_source_return_net_error() throws NetworkErrorException &#123;
        //given
        FileListContract.View mockView = mock(FileListContract.View.class);
        FileDataSource mockFileDataSource = mock(FileDataSource.class);
        when(mockFileDataSource.getFileList()).thenThrow(new NetworkErrorException());
        FileListContract.FilePresenter filePresenter = new FilePresenterImpl(mockFileDataSource, mockView);
        //when
        filePresenter.getFileList();
        //then
        verify(mockView).showNetWorkException("NetworkErrorException");
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以通过查看Coverage查看逻辑的覆盖情况，判断是否有重要的逻辑遗漏。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b5ff0f4675841c899473f5f0c4ee025~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1b81a61c179407b96eb0b41989bdfb1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后我们运行file bundle所有的测试，报告如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e195ae6e3b0f426eaa2c6d2d8a3d1e3d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">6.集成验收测试</h2>
<ol>
<li>file bundle模块发布1.0.1版本</li>
</ol>
<pre><code class="copyable">implementation 'com.cloud.disk.bundle:file:1.0.1'
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>执行守护测试</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/939949c16c824747bdb0bade6e6d9068~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>运行检查</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0846861f29149ad990a2c1d951be2a6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-10">总结</h1>
<p>本篇介绍了文件模块团队将文件主页重构为MVP架构，并且补充了自动化测试。经过重构后，团队的开发效率和版本质量有了明显的提升。有了文件模块的打样，给其他团队带来了很大的信心。</p>
<p>接下来，我们将继续分享动态模块的重构之旅。与文件模块不一样的是动态模块决定采用Kotlin+MVVM架构。</p>
<p>下一篇，单体移动应用“模块化”演进之旅（14）- Kotlin+MVVM重构示例篇</p>
<h1 data-id="heading-11">CloudDisk示例代码</h1>
<p><a href="https://github.com/junbin1011/CloudDisk" target="_blank" rel="nofollow noopener noreferrer">CloudDisk</a></p>
<h1 data-id="heading-12">系列链接</h1>
<p><a href="https://juejin.cn/post/6943470229905211422" target="_blank">移动应用遗留系统重构（1）- 开篇</a></p>
<p><a href="https://juejin.cn/post/6945313969556946980" target="_blank">移动应用遗留系统重构（2）-架构篇</a></p>
<p><a href="https://juejin.cn/post/6947855094272491556" target="_blank">移动应用遗留系统重构（3）-示例篇</a></p>
<p><a href="https://juejin.cn/post/6950077521790500894" target="_blank">移动应用遗留系统重构（4）-分析篇</a></p>
<p><a href="https://juejin.cn/post/6952298178095874055" target="_blank">移动应用遗留系统重构（5）- 重构方法篇</a></p>
<p><a href="https://juejin.cn/post/6954635678982340622" target="_blank">移动应用遗留系统重构（6）- 测试篇</a></p>
<p><a href="https://juejin.cn/post/6959504791642832909" target="_blank">移动应用遗留系统重构（7）- 解耦重构演示篇(一)+视频演示</a></p>
<p><a href="https://juejin.cn/post/6963214120178941983" target="_blank">移动应用遗留系统重构（8）- 依赖注入篇</a></p>
<p><a href="https://juejin.cn/post/6966166367821103117" target="_blank">移动应用遗留系统重构（9）- 路由篇</a></p>
<p><a href="https://juejin.cn/post/6970870458660945934" target="_blank">移动应用遗留系统重构（10）- 解耦重构演示篇（二）</a></p>
<p><a href="https://juejin.cn/post/6973836199655899149" target="_blank">移动应用遗留系统重构（11）- 制品管理篇</a></p>
<p><a href="https://juejin.cn/post/6974634615537401886" target="_blank">移动应用遗留系统重构（12）- 编译调试篇</a></p>
<h1 data-id="heading-13">大纲</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8adefb4375440a8b496b95540cc30ee~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-14">关于</h1>
<ul>
<li>作者：黄俊彬</li>
<li><a href="https://junbin.tech/" target="_blank" rel="nofollow noopener noreferrer">博客：junbin.tech</a></li>
<li><a href="https://github.com/junbin1011" target="_blank" rel="nofollow noopener noreferrer">GitHub: junbin1011 </a></li>
<li><a href="https://www.zhihu.com/people/junbin-9-77" target="_blank" rel="nofollow noopener noreferrer">知乎: @JunBin</a></li>
</ul></div>  
</div>
            