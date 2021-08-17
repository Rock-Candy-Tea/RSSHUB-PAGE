
---
title: 'Android Jetpack系列--4.DataBinding使用详解'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=974'
author: 掘金
comments: false
date: Sun, 15 Aug 2021 21:43:11 GMT
thumbnail: 'https://picsum.photos/400/300?random=974'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">定义</h3>
<ul>
<li>即数据绑定，使数据对象和xml布局绑定,支持双向绑定，是Android团队实现MVVM架构的一种方法；</li>
</ul>
<h3 data-id="heading-1">优点</h3>
<ol>
<li>省去大量模板代码：findViewById，onClickListener,setText等；</li>
<li>使view与逻辑解耦，不用向MVC那样混乱，也不用向MVP那样定义大量接口；</li>
<li>view与数据对象双向绑定，开发时只需关注数据对象，无需关系view的各种操作；</li>
<li>xml中可以完成简单逻辑（尽量不要在xml中实现逻辑）；</li>
</ol>
<h3 data-id="heading-2">简单使用</h3>
<ol>
<li>开启DataBinding支持，在module的build.gradle中加入下面代码并sync project;</li>
</ol>
<pre><code class="copyable">android &#123;
    ...
    dataBinding &#123;
        enabled = true
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>创建一个数据类ArticleItem.kt</li>
</ol>
<pre><code class="copyable">data class ArticleItem(val title:String, val author:String,val content:String,)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>创建一个Activity，并自动生成布局，在布局文件中将光标移动到根View上，按alt+enter，选择弹出菜单的「Convert to data binding layout」，代码如下：</li>
</ol>
<pre><code class="copyable"><?xml version="1.0" encoding="utf-8"?>
<layout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools">

    //在data标签当中声明要使用到的变量、类的全路径
    <data>
        <variable
            name="articleInfo"
            type="com.jinyang.jetpackdemo.bean.ArticleItem" />
    </data>

    <androidx.constraintlayout.widget.ConstraintLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        tools:context=".activity.ArticleListActivity">

        <TextView
            android:id="@+id/tv_article_title"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            //通过@&#123;articleInfo.title&#125;可以为textView引入对应的变量，还可以用default设置默认值
            android:text="@&#123;articleInfo.title,default=DataBinding使用详解&#125;"
            android:textColor="#000000"
            android:textSize="20sp"
            android:textStyle="bold"
            app:layout_constraintLeft_toLeftOf="parent"
            app:layout_constraintTop_toTopOf="parent" />

        <TextView
            android:id="@+id/tv_article_author"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@&#123;articleInfo.author,default=JinYang&#125;"
            android:textColor="#666666"
            android:textSize="14sp"
            app:layout_constraintLeft_toLeftOf="parent"
            app:layout_constraintTop_toBottomOf="@+id/tv_article_title" />

        <TextView
            android:id="@+id/tv_article_content"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:ellipsize="end"
            android:lines="2"
            android:text="@&#123;articleInfo.content,default=即数据绑定使数据对象和xml布局绑定支持双向绑定是Android团队实现MVVM架构的一种方法&#125;"
            android:textColor="#333333"
            android:textSize="18sp"
            app:layout_constraintLeft_toLeftOf="parent"
            app:layout_constraintRight_toRightOf="parent"
            app:layout_constraintTop_toBottomOf="@+id/tv_article_author" />

    </androidx.constraintlayout.widget.ConstraintLayout>
</layout>

// 为方便ArticleItem的复用，也可以用import方式引入
<data>
    <import type="com.jinyang.jetpackdemo.bean.ArticleItem"/>
    <variable
        name="articleInfo"
        type="ArticleItem" />
</data>

// 为防止重复还可以为import增加别名
<data>
    <import
        alias="ArticleInfo"
        type="com.jinyang.jetpackdemo.bean.ArticleItem" />
    <variable
        name="articleInfo"
        type="ArticleInfo" />
</data>
//binding类的名称默认是已布局文件名改完驼峰命名法生成的如：ActivityArticleListBinding
//可以通过如下方式自定义 ViewDataBinding 的实例名
<data class="ArticleListBinding">
    ...
</data>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>在Activity中为articleInfo赋值</li>
</ol>
<pre><code class="copyable">class ArticleListActivity : AppCompatActivity() &#123;
    override fun onCreate(savedInstanceState: Bundle?) &#123;
        super.onCreate(savedInstanceState)
<!--         val binding: ArticleListBinding = -->
        val binding: ActivityArticleListBinding =
            DataBindingUtil.setContentView(this, R.layout.activity_article_list)
        binding.articleInfo= ArticleItem("Android Jetpack系列","今阳",
            "Jetpack 是一个由多个库组成的套件;\n" +
                    "主要包括架构（Architecture）、基础（Foundation）、行为（Behavior） 、界面（UI）四个方面；")
    &#125;
&#125;

//DataBinding也支持在Fragment和RecyclerView中使用
@Override
public View onCreateView(@NonNull LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) &#123;
    binding = DataBindingUtil.inflate(inflater, getContentViewId(), container, false);
    return binding.getRoot();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">单向数据绑定</h3>
<ul>
<li>默认情况下，普通函数和字符串是不可观察的，这就意味着，当您在数据绑定布局中需要使用它们时，只能在新建的时候获取它们的值，但在后续的操作中，却不能得到相应的数据。</li>
<li>Observable有三种实现：BaseObservable、ObservableField、ObservableCollection</li>
</ul>
<h4 data-id="heading-4">BaseObservable</h4>
<ul>
<li>BaseObservable 提供了 notifyChange()（刷新所有的值域）和 notifyPropertyChanged()（只更新对应 BR，该BR通过注释 @Bindable 生成）两个方法；</li>
</ul>
<pre><code class="copyable">//1. 自定义Observable
class ArticleItem2(var title: String, author: String, content: String) :
    BaseObservable() &#123;

    @get:Bindable
    var author: String = author
        set(value) &#123;
            field = value
            notifyPropertyChanged(BR.author)
        &#125;

    @get:Bindable
    var content: String = content
        set(value) &#123;
            field = value
            notifyChange()
        &#125;
&#125;
2. Activity中创建点击事件调用ArticleItem2的set方法
class ArticleListActivity : AppCompatActivity() &#123;
     lateinit var articleInfo: ArticleItem2
    override fun onCreate(savedInstanceState: Bundle?) &#123;
        super.onCreate(savedInstanceState)
        val binding: ActivityArticleListBinding =
            DataBindingUtil.setContentView(this, R.layout.activity_article_list)
        articleInfo = ArticleItem2(
            "Android Jetpack系列", "今阳",
            "Jetpack 是一个由多个库组成的套件;"
        )
        //可以设置监听器观察属性的更改
        articleInfo.addOnPropertyChangedCallback(object : Observable.OnPropertyChangedCallback() &#123;
            override fun onPropertyChanged(sender: Observable, propertyId: Int) &#123;
                when &#123;
                    BR.author == propertyId -> &#123;
                        LjyLogUtil.d("BR.author")
                    &#125;
                    BR.content == propertyId -> &#123;
                        LjyLogUtil.d("BR.content")
                    &#125;
                    BR._all == propertyId -> &#123;
                        LjyLogUtil.d("BR._all")
                    &#125;
                    else -> &#123;
                        LjyLogUtil.d("propertyId:$propertyId")
                    &#125;
                &#125;
            &#125;
        &#125;)
        binding.articleInfo=articleInfo
        binding.onClickPresenter=OnClickPresenter()
    &#125;

    inner class OnClickPresenter &#123;
        fun changeTitle() &#123;
            articleInfo.title="$&#123;articleInfo.title&#125;1"
        &#125;
        fun changeAuthor() &#123;
            articleInfo.author="$&#123;articleInfo.author&#125;1"
        &#125;
        fun changeContent() &#123;
            articleInfo.content="$&#123;articleInfo.content&#125;1"
        &#125;
    &#125;
&#125;
//3.xml中增加button并调用点击事件
<?xml version="1.0" encoding="utf-8"?>
<layout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools">

    <data >
        <variable
            name="articleInfo"
            type="com.jinyang.jetpackdemo.bean.ArticleItem2" />
        <variable
            name="onClickPresenter"
            type="com.jinyang.jetpackdemo.activity.ArticleListActivity.OnClickPresenter" />
    </data>

    <androidx.constraintlayout.widget.ConstraintLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        tools:context=".activity.ArticleListActivity">

        <TextView
            android:id="@+id/tv_article_title"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@&#123;articleInfo.title,default=DataBinding使用详解&#125;"
            android:textColor="#000000"
            android:textSize="20sp"
            android:textStyle="bold"
            app:layout_constraintLeft_toLeftOf="parent"
            app:layout_constraintTop_toTopOf="parent" />

        <TextView
            android:id="@+id/tv_article_author"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@&#123;articleInfo.author,default=JinYang&#125;"
            android:textColor="#666666"
            android:textSize="14sp"
            app:layout_constraintLeft_toLeftOf="parent"
            app:layout_constraintTop_toBottomOf="@+id/tv_article_title" />

        <TextView
            android:id="@+id/tv_article_content"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:ellipsize="end"
            android:lines="2"
            android:text="@&#123;articleInfo.content,default=即数据绑定使数据对象和xml布局绑定支持双向绑定是Android团队实现MVVM架构的一种方法&#125;"
            android:textColor="#333333"
            android:textSize="16sp"
            app:layout_constraintLeft_toLeftOf="parent"
            app:layout_constraintRight_toRightOf="parent"
            app:layout_constraintTop_toBottomOf="@+id/tv_article_author" />

        <Button
            android:id="@+id/btn_title"
            android:layout_width="wrap_content"
            android:text="title+1"
            android:textAllCaps="false"
            app:layout_constraintLeft_toLeftOf="parent"
            android:onClick="@&#123;()->onClickPresenter.changeTitle()&#125;"
            app:layout_constraintTop_toBottomOf="@+id/tv_article_content"
            android:layout_margin="10dp"
            android:layout_height="wrap_content"/>
        <Button
            android:id="@+id/btn_author"
            android:layout_width="wrap_content"
            android:text="author+1"
            android:textAllCaps="false"
            app:layout_constraintLeft_toRightOf="@id/btn_title"
            android:layout_margin="10dp"
            app:layout_constraintTop_toBottomOf="@+id/tv_article_content"
            android:onClick="@&#123;()->onClickPresenter.changeAuthor()&#125;"
            android:layout_height="wrap_content"/>
        <Button
            android:id="@+id/btn_content"
            app:layout_constraintLeft_toRightOf="@id/btn_author"
            android:onClick="@&#123;()->onClickPresenter.changeContent()&#125;"
            android:layout_width="wrap_content"
            android:layout_margin="10dp"
            android:text="content+1"
            android:textAllCaps="false"
            app:layout_constraintTop_toBottomOf="@+id/tv_article_content"
            android:layout_height="wrap_content"/>
    </androidx.constraintlayout.widget.ConstraintLayout>
</layout>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">ObservableField</h4>
<ul>
<li>继承BaseObservable限制较高，需要notify操作，为了使用方便可以使用ObservableField；</li>
<li>是官方对 BaseObservable 中字段的注解和刷新等操作的封装；</li>
<li>官方原生提供了对基本数据类型的封装，例如 ObservableBoolean、ObservableByte、ObservableChar、ObservableShort、ObservableInt、ObservableLong、ObservableFloat、ObservableDouble 以及 ObservableParcelable ；</li>
<li>也可通过 ObservableField 泛型来申明其他类型</li>
</ul>
<pre><code class="copyable">//1. 定义数据类
class ArticleItem3(title: String, author: String, content: String) &#123;
    val title: ObservableField<String> = ObservableField<String>(title)
    val author: ObservableField<String> = ObservableField<String>(author)
    val content: ObservableField<String> = ObservableField<String>(content)
&#125;
//2. 修改OnClickPresenter代码
inner class OnClickPresenter &#123;
    fun changeTitle() &#123;
        articleInfo.title.set("$&#123;articleInfo.title.get()&#125;1")
    &#125;

    fun changeAuthor() &#123;
        articleInfo.author.set("$&#123;articleInfo.author.get()&#125;1")
    &#125;

    fun changeContent() &#123;
        articleInfo.content.set("$&#123;articleInfo.content.get()&#125;1")
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">ObservableCollection</h4>
<ul>
<li>dataBinding 也提供了包装类用于替代原生的 List 和 Map，分别是 ObservableList 和 ObservableMap</li>
</ul>
<pre><code class="copyable">//1. 修改variable标签
<data >
    <variable
        name="articleInfo"
        type="androidx.databinding.ObservableMap&lt;String,String&gt;" />
    <variable
        name="onClickPresenter"
        type="com.jinyang.jetpackdemo.activity.ArticleListActivity.OnClickPresenter" />
</data>
//2. 修改Activity中的代码
class ArticleListActivity : AppCompatActivity() &#123;
    lateinit var articleInfo: ObservableArrayMap<String, String>
    override fun onCreate(savedInstanceState: Bundle?) &#123;
        super.onCreate(savedInstanceState)
        val binding: ActivityArticleListBinding =
            DataBindingUtil.setContentView(this, R.layout.activity_article_list)

        articleInfo = ObservableArrayMap()
        articleInfo.apply &#123;
            put("title", "Android Jetpack系列")
            put("author", "今阳")
            put("content", "Jetpack 是一个由多个库组成的套件;")
        &#125;

        binding.articleInfo = articleInfo
        binding.onClickPresenter = OnClickPresenter()
    &#125;

    inner class OnClickPresenter &#123;
        fun changeTitle() &#123;
            articleInfo["title"]+="1"
        &#125;

        fun changeAuthor() &#123;
            articleInfo["author"]+="1"
        &#125;

        fun changeContent() &#123;
            articleInfo["content"]+="1"
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">双向数据绑定</h3>
<ul>
<li>当数据改变时同时使视图刷新，而视图改变时也可以同时改变数据</li>
<li>绑定变量的方式比单向绑定多了一个等号,代码如下：</li>
</ul>
<pre><code class="copyable"><EditText
    android:id="@+id/edit_content"
    android:layout_width="match_parent"
    android:text="@=&#123;articleInfo.content&#125;"
    android:layout_height="wrap_content"/>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">LiveData 替换 Observable Fields</h3>
<ul>
<li>上面讲了Observable Fields，但是google官方更推荐使用LiveData 替换 Observable Field;</li>
<li>参考google官方文章<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F133949967" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/133949967" ref="nofollow noopener noreferrer">两步使用 LiveData 替换 Observable Field</a></li>
<li>LiveData 可以感知生命周期，这一点与 Observable Fields 相比并没有多大优势，因为 Data Binding 原本就可以检查视图活跃情况。</li>
</ul>
<p>因此对于 LiveData 来说，它的优势在于不仅支持Transformations，而且可以与许多架构组件 (如Room、WorkManager) 相互配合使用。
综上，我们推荐您使用 LiveData。方法也非常简单，只需要两个步骤。</p>
<pre><code class="copyable">//1. 用 LiveData 替换 Observable Fields
class ArticleItem4(title: String, author: String, content: String) : ViewModel() &#123;
    var title: MutableLiveData<String> = MutableLiveData<String>().apply &#123; value = title &#125;
    var author: MutableLiveData<String> = MutableLiveData<String>().apply &#123; value = author &#125;
    var content: MutableLiveData<String> = MutableLiveData<String>().apply &#123; value = content &#125;
&#125;
//2. 设置 LiveData 的生命周期所有者(lifecycleOwner)
class ArticleListActivity : AppCompatActivity() &#123;
    lateinit var articleInfo: ArticleItem4
    override fun onCreate(savedInstanceState: Bundle?) &#123;
        super.onCreate(savedInstanceState)

        val binding: ActivityArticleListBinding =
            DataBindingUtil.setContentView(this, R.layout.activity_article_list)

        //视图的绑定类中包含一个 setLifecycleOwner 方法，想要从数据绑定布局观察 LiveData ，必须使用该方法。
        binding.lifecycleOwner = this

        articleInfo = ArticleItem4(
            "Android Jetpack系列", "今阳",
            "Jetpack 是一个由多个库组成的套件;"
        )
        binding.articleInfo = articleInfo
        binding.onClickPresenter = OnClickPresenter()
    &#125;

    inner class OnClickPresenter &#123;
        fun changeTitle() &#123;
            articleInfo.title.value+="6"
        &#125;

        fun changeAuthor() &#123;
            articleInfo.author.value+="6"
        &#125;

        fun changeContent() &#123;
            articleInfo.content.value+="6"
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">事件绑定</h3>
<ul>
<li>事件绑定也是一种变量绑定，只不过设置的变量是回调接口而已，而且我们上面的举例中button的点击事件已有用到</li>
</ul>
<pre><code class="copyable">//1. 定义事件方法
inner class OnClickPresenter &#123;
    fun changeTitle(articleInfo:ArticleItem4) &#123;
        articleInfo.title.value+="6"
    &#125;

    fun changeAuthor() &#123;
        articleInfo.author.value+="6"
    &#125;
&#125;
//2. data中引用
<data >
    <variable
        name="articleInfo"
        type="com.jinyang.jetpackdemo.bean.ArticleItem4" />
    <variable
        name="onClickPresenter"
        type="com.jinyang.jetpackdemo.activity.ArticleListActivity.OnClickPresenter" />
</data>
//3. view中绑定
<Button
    android:id="@+id/btn_title"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="title+1"
    android:onClick="@&#123;()->onClickPresenter.changeTitle(articleInfo)&#125;"
    />
<Button
    android:id="@+id/btn_author"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="author+1"
    android:onClick="@&#123;()->onClickPresenter.changeAuthor()&#125;"
    />
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">BindingAdapter 和 BindingConversion</h3>
<h4 data-id="heading-11">BindingAdapter</h4>
<ul>
<li>dataBinding 提供了 BindingAdapter 这个注解用于支持自定义属性，或者是修改原有属性；</li>
<li>注解值可以是已有的 xml 属性，例如 android:src、android:text等，也可以自定义属性然后在 xml 中使用；</li>
<li>例1：为每个 Button 的文本都要加上后缀：“-Button”</li>
</ul>
<pre><code class="copyable">//1. 定义一个方法，类似于扩展函数
class ArticleListActivity : AppCompatActivity() &#123;
    override fun onCreate(savedInstanceState: Bundle?) &#123;
        super.onCreate(savedInstanceState)
        val binding: ActivityArticleListBinding =
            DataBindingUtil.setContentView(this, R.layout.activity_article_list)
        binding.lifecycleOwner = this
        var articleInfo: ArticleItem4 = ArticleItem4(
            "Android Jetpack系列", "今阳",
            "Jetpack 是一个由多个库组成的套件;"
        )
        binding.articleInfo = articleInfo
    &#125;
&#125;

@BindingAdapter("android:text")
fun setText(view: Button, text: String) &#123;
    view.text = "$text-Button"
&#125;

//2. xml中设置android:text='@&#123;"title+1"&#125;'
<Button
    android:id="@+id/btn_title"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text='@&#123;"title+1"&#125;'
    android:onClick="@&#123;()->onClickPresenter.changeTitle(articleInfo)&#125;"
    />
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>例2：自定义属性</li>
<li>这里借助一个Google 官推的图片库 Coil，这个库完全是用 Kotlin 写的，而且运用了大量 Kotlin 的特性，尤其是协程；</li>
<li>Coil 给 ImageView 加了很多拓展函数，所以我们一行代码便能进行图片加载；</li>
<li>详细使用可以参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FCG5O-wMIKIjGWW8XNQsaKg" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/CG5O-wMIKIjGWW8XNQsaKg" ref="nofollow noopener noreferrer">还在用 Glide？看看 Google 官推的图片库 Coil 有何不同！</a></li>
</ul>
<pre><code class="copyable">//1. 添加coil依赖
implementation("io.coil-kt:coil:1.1.1")
//2. 创建辅助的数据类
class ImageBean(url: String) &#123;
    var url: MutableLiveData<String> = MutableLiveData<String>().apply &#123; value = url &#125;
&#125;
//3.定义方法并添加注解
@BindingAdapter("url")
fun loadImage(view: ImageView, url: String) &#123;
    view.load(url)
    LjyLogUtil.d("url:$&#123;url&#125;")
&#125;
//4. xml中引用
<variable
    name="image"
    type="com.jinyang.jetpackdemo.bean.ImageBean" />
//5. ImageView中使用
 <ImageView
    app:layout_constraintTop_toBottomOf="@+id/edit_content"
    app:layout_constraintLeft_toLeftOf="parent"
    app:layout_constraintRight_toRightOf="parent"
    android:src="@mipmap/ic_launcher"
    android:layout_width="wrap_content"
    app:url="@&#123;image.url&#125;"
    android:layout_height="wrap_content"/>
//6. activity代码
lass ArticleListActivity : AppCompatActivity() &#123;
    lateinit var articleInfo: ArticleItem4
    lateinit var image: ImageBean
    override fun onCreate(savedInstanceState: Bundle?) &#123;
        super.onCreate(savedInstanceState)
        val binding: ActivityArticleListBinding =
            DataBindingUtil.setContentView(this, R.layout.activity_article_list)
        binding.lifecycleOwner = this
        articleInfo = ArticleItem4(
            "Android Jetpack系列", "今阳",
            "Jetpack 是一个由多个库组成的套件;"
        )
        binding.articleInfo = articleInfo
        image = ImageBean("https://pic1.zhimg.com/v2-dc32dcddfd7e78e56cc4b6f689a24979_is.jpg")
        binding.image=image
        binding.onClickPresenter = OnClickPresenter()
    &#125;

    inner class OnClickPresenter &#123;
        fun changeTitle(articleInfo: ArticleItem4) &#123;
            articleInfo.title.value += "6"
            image.url.value="https://pic3.zhimg.com/v2-e5656460688d19f7358ab3a6055fe34a_720w.jpg?source=95cc6b4a"
        &#125;

        fun changeAuthor() &#123;
            articleInfo.author.value += "6"
            image.url.value="https://pic2.zhimg.com/v2-f6981776beae87401991b426fbe34fdd_720w.jpg?source=95cc6b4a"
        &#125;

        fun changeContent() &#123;
            articleInfo.content.value += "6"
            image.url.value="https://pic2.zhimg.com/v2-f2eddc2fe0e509de5bbeeb351ddc2c61_1440w.jpg?source=172ae18b"
        &#125;
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">BindingConversion</h4>
<ul>
<li>dataBinding 还支持对数据进行转换，或者进行类型转换</li>
</ul>
<pre><code class="copyable">@BindingConversion
fun convertStringToDrawable(str: String): Drawable &#123;
    return when (str) &#123;
        "红色" -> &#123;
            ColorDrawable(Color.parseColor("#FF4081"))
        &#125;
        "蓝色" -> &#123;
            ColorDrawable(Color.parseColor("#3F51B5"))
        &#125;
        else -> &#123;
            ColorDrawable(Color.parseColor("#344567"))
        &#125;
    &#125;
&#125;

@BindingConversion
fun convertStringToColor(str: String): Int &#123;
    return when (str) &#123;
        "红色" -> &#123;
            Color.parseColor("#FF4081")
        &#125;
        "蓝色" -> &#123;
            Color.parseColor("#3F51B5")
        &#125;
        else -> &#123;
            Color.parseColor("#344567")
        &#125;
    &#125;
&#125;

<Button
    android:id="@+id/btn_title"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:background='@&#123;"蓝色"&#125;'
    android:textColor='@&#123;"红色",default=@color/colorAccent&#125;'
    android:text="title+1"
    android:onClick="@&#123;()->onClickPresenter.changeTitle(articleInfo)&#125;"
    />
<Button
    android:id="@+id/btn_author"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:background='@&#123;"蓝色"&#125;'
    android:textColor='@&#123;"红色"&#125;'
    android:text="author+1"
    android:onClick="@&#123;()->onClickPresenter.changeAuthor()&#125;"
    />
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">绑定列表数据</h3>
<ul>
<li>RecyclerView使用BaseRecyclerViewAdapterHelper+DataBinding</li>
</ul>
<ol>
<li>自定义Adapter：</li>
</ol>
<pre><code class="copyable">class ArticleAdapter(data: MutableList<ArticleItem4>?) :
    BaseQuickAdapter<ArticleItem4, ArticleItemViewHolder>(R.layout.layout_item_article, data) &#123;

    override fun convert(holder: ArticleItemViewHolder, item: ArticleItem4) &#123;
        holder.binding?.articleInfo = item
        holder.binding?.executePendingBindings()
    &#125;

    class ArticleItemViewHolder(view: View) : BaseViewHolder(view) &#123;
        val binding: LayoutItemArticleBinding? = DataBindingUtil.bind(view)
    &#125;
&#125;

//最新的BaseQuickAdapter提供了上述自定义ViewHolder的实现，BaseDataBindingHolder，可以如下使用：
class ArticleAdapter(data: MutableList<ArticleItem4>?) :
    BaseQuickAdapter<ArticleItem4,  BaseDataBindingHolder<LayoutItemArticleBinding> >(R.layout.layout_item_article, data) &#123;

    override fun convert(holder: BaseDataBindingHolder<LayoutItemArticleBinding>, item: ArticleItem4) &#123;
        holder.dataBinding?.articleInfo = item
        holder.dataBinding?.executePendingBindings()
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>layout_item_article.xml布局</li>
</ol>
<pre><code class="copyable"><?xml version="1.0" encoding="utf-8"?>
<layout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto">

    <data>
        <variable
            name="articleInfo"
            type="com.jinyang.jetpackdemo.bean.ArticleItem4" />
    </data>

    <androidx.constraintlayout.widget.ConstraintLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content">

        <TextView
            android:id="@+id/tv_article_title"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@&#123;articleInfo.title,default=titleText&#125;"
            android:textColor="#000000"
            android:textSize="20sp"
            android:textStyle="bold"
            app:layout_constraintLeft_toLeftOf="parent"
            app:layout_constraintTop_toTopOf="parent" />

        <TextView
            android:id="@+id/tv_article_author"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@&#123;articleInfo.author,default=authorText&#125;"
            android:textColor="#666666"
            android:textSize="14sp"
            app:layout_constraintLeft_toLeftOf="parent"
            app:layout_constraintTop_toBottomOf="@+id/tv_article_title" />

        <TextView
            android:id="@+id/tv_article_content"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:ellipsize="end"
            android:lines="2"
            android:text="@&#123;articleInfo.content,default=contentText&#125;"
            android:textColor="#333333"
            android:textSize="16sp"
            app:layout_constraintLeft_toLeftOf="parent"
            app:layout_constraintRight_toRightOf="parent"
            app:layout_constraintTop_toBottomOf="@+id/tv_article_author" />
    </androidx.constraintlayout.widget.ConstraintLayout>
</layout>

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>Activity代码如下</li>
</ol>
<pre><code class="copyable">class ArticleList2Activity : AppCompatActivity() &#123;
    lateinit var mAdapter:ArticleAdapter
    override fun onCreate(savedInstanceState: Bundle?) &#123;
        super.onCreate(savedInstanceState)
        LjyLogUtil.d("onCreate")
        val binding: ActivityArticleList2Binding =
            DataBindingUtil.setContentView(this, R.layout.activity_article_list2)
        binding.lifecycleOwner = this
        binding.rvArticleList.layoutManager = LinearLayoutManager(this)
        val articleList:MutableList<ArticleItem4> = ArrayList()
        articleList.add(ArticleItem4("title1","jinYang","content111"))
        articleList.add(ArticleItem4("title2","jinYang","content222"))
        articleList.add(ArticleItem4("title3","jinYang","content333"))
        mAdapter= ArticleAdapter(articleList)
        binding.rvArticleList.adapter=mAdapter
        binding.onClickPresenter2 = OnClickPresenter2()
    &#125;

    inner class OnClickPresenter2 &#123;
        fun addArticle() &#123;
            mAdapter.addData(ArticleItem4("title$&#123;mAdapter.data.size&#125;","jinYang","content$&#123;mAdapter.data.size&#125;"))
            LjyLogUtil.d("addArticle")
        &#125;

        fun removeArticle() &#123;
            mAdapter.removeAt(0)
            LjyLogUtil.d("removeArticle")
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>activity_article_list2.xml布局如下</li>
</ol>
<pre><code class="copyable"><?xml version="1.0" encoding="utf-8"?>
<layout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools">
    <data>
        <variable
            name="onClickPresenter2"
            type="com.jinyang.jetpackdemo.activity.ArticleList2Activity.OnClickPresenter2" />
    </data>
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:orientation="vertical"
        tools:context=".activity.ArticleList2Activity">
        <Button
            android:id="@+id/btn_add"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:onClick="@&#123;()->onClickPresenter2.addArticle()&#125;"
            android:text="addArticle" />
        <Button
            android:id="@+id/btn_remove"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:onClick="@&#123;()->onClickPresenter2.removeArticle()&#125;"
            android:text="removeArticle" />
        <androidx.recyclerview.widget.RecyclerView
            android:id="@+id/rv_article_list"
            android:layout_width="match_parent"
            android:layout_height="match_parent" />
    </LinearLayout>
</layout>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">我是今阳，如果想要进阶和了解更多的干货，欢迎关注微信公众号 “今阳说” 接收我的最新文章</h2></div>  
</div>
            