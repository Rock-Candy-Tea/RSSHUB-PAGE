
---
title: 'RecycleView 横向滑动指示器'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/10437245-7c5ea30c3d6e8994.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/10437245-7c5ea30c3d6e8994.png'
---

<div>   
<h1>项目中需要添加类似京东 淘宝首页商品滑动 下面的指示器跟随随便位移对应进度。具体效果如下：</h1>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1080" data-height="2160"><img data-original-src="//upload-images.jianshu.io/upload_images/10437245-7c5ea30c3d6e8994.png" data-original-width="1080" data-original-height="2160" data-original-format="image/png" data-original-filesize="1057242" src="https://upload-images.jianshu.io/upload_images/10437245-7c5ea30c3d6e8994.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">Screenshot_2020-06-24-15-15-39-138_com.xueersi.pa.png</div>
</div>
<h1>具体实现demo效果：</h1>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1080" data-height="2160"><img data-original-src="//upload-images.jianshu.io/upload_images/10437245-b96cd2d408c94dec.png" data-original-width="1080" data-original-height="2160" data-original-format="image/png" data-original-filesize="39567" src="https://upload-images.jianshu.io/upload_images/10437245-b96cd2d408c94dec.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">Screenshot_2020-06-24-15-30-30-516_com.yunlei.hin.png</div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1080" data-height="2160"><img data-original-src="//upload-images.jianshu.io/upload_images/10437245-41815d6b5ac2216b.png" data-original-width="1080" data-original-height="2160" data-original-format="image/png" data-original-filesize="38661" src="https://upload-images.jianshu.io/upload_images/10437245-41815d6b5ac2216b.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">Screenshot_2020-06-24-15-30-35-924_com.yunlei.hin.png</div>
</div>
<h1>1、分析</h1>
<p>其实这个很简单，主要就是有以下几点</p>
<ul>
<li>1.绘制一个圆角矩形做背景；</li>
<li>2.绘制一个圆角矩形做背景；</li>
<li>3 .绘制一个圆角矩形做指示器；</li>
<li>4.确定指示器的长度和指示器的位置；</li>
<li>5.根据RecyclerView滑动的距离动态改变指示器的位置。</li>
</ul>
<h1>2、绘制指示器</h1>
<p>绘制背景的圆角矩形的时候，不考虑padding信息，就很简单</p>
<pre><code> override fun onSizeChanged(w: Int, h: Int, oldw: Int, oldh: Int) &#123;
        super.onSizeChanged(w, h, oldw, oldh)
        viewWidth = w
        mBgRect.set(0f, 0f, w * 1f, h * 1f)
        mRadius = h / 2f
    &#125;

    override fun onDraw(canvas: Canvas?) &#123;
        super.onDraw(canvas)
        //绘制背景
        canvas?.drawRoundRect(mBgRect, mRadius, mRadius, mBgPaint)
    &#125;
</code></pre>
<p>绘制指示器</p>
<blockquote>
<p>ratio指的是指示器长度，即如果滚动内容有两屏，则指示器应该为1/2长度，以此类推 （当然上面所示app不一定实现了这个，可能会为了美观设置一个固定比例）</p>
</blockquote>
<p>progress指的是滑动距离和指示器对应关系，这个实际上就是滑动进度条的意思</p>
<pre><code> //计算指示器的长度和位置
    val leftOffset = viewWidth * (1f - ratio) * progress
    val left = mBgRect.left + leftOffset
    val right = left + viewWidth * ratio
    mRect.set(left, mBgRect.top, right, mBgRect.bottom)

    //绘制指示器
    canvas?.drawRoundRect(mRect, mRadius, mRadius, mPaint)
</code></pre>
<h1>3、和RecyclerView联动</h1>
<p>获取RecyclerView滚动的位置可根据以下几个方法获取</p>
<ul>
<li><ol>
<li>computeVerticalScrollExtent()/computeHorizontalScrollExtent//当前RcyclerView显示区域的高度。水平列表屏幕从左侧到右侧显示范围</li>
</ol></li>
<li><ol start="2">
<li>computeVerticalScrollOffset()/computeHorizontalScrollOffset //已经向下滚动的距离，为0时表示已处于顶部。</li>
</ol></li>
<li><ol start="3">
<li>computeVerticalScrollRange()/computeHorizontalScrollRange //整体的高度，注意是整体，包括在显示区域之外的</li>
</ol></li>
</ul>
<p>监听滑动，配合上诉方法就可以拿到滑动位置的比例</p>
<pre><code> recyclerView.addOnScrollListener(object : RecyclerView.OnScrollListener() &#123;
        override fun onScrolled(recyclerView: RecyclerView, dx: Int, dy: Int) &#123;
            super.onScrolled(recyclerView, dx, dy)
            val offsetX = recyclerView.computeHorizontalScrollOffset()
            val range = recyclerView.computeHorizontalScrollRange()
            val extend = recyclerView.computeHorizontalScrollExtent()
            val progress: Float = offsetX * 1.0f / (range - extend)     //因为指示器有长度，所以这里需要减去首屏长度
            this@HIndicator.progress = progress     //设置滚动距离所占比例
        &#125;
    &#125;)
</code></pre>
<p>具体实现逻辑：</p>
<pre><code>
class TreeIndicator @JvmOverloads constructor(
    context: Context, attrs: AttributeSet? = null, defStyleAttr: Int = 0
) : View(context, attrs, defStyleAttr) &#123;

    private val mBgPaint: Paint = Paint(Paint.ANTI_ALIAS_FLAG)
    private val mBgRect: RectF = RectF()
    private var mRadius: Float = 0f
    private val mPaint: Paint = Paint(Paint.ANTI_ALIAS_FLAG)
    private var mRect: RectF = RectF()
    private var viewWidth: Int = 0
    private var mBgColor = Color.parseColor("#e5e5e5")
    private var mIndicatorColor = Color.parseColor("#ff4646")
    var ratio = 0.5f        //长度比例
        set(value) &#123;
            field = value
            invalidate()
        &#125;
    var progress: Float = 0f    //滑动进度比例
        set(value) &#123;
            field = value
            invalidate()
        &#125;

    init &#123;

        val typedArray: TypedArray = context.obtainStyledAttributes(attrs, R.styleable.HIndicator)
        mBgColor = typedArray.getColor(R.styleable.HIndicator_hi_bgColor, mBgColor)
        mIndicatorColor =
            typedArray.getColor(R.styleable.HIndicator_hi_indicatorColor, mIndicatorColor)
        typedArray.recycle()

        mBgPaint.color = mBgColor
        mBgPaint.style = Paint.Style.FILL
        mPaint.color = mIndicatorColor
        mPaint.style = Paint.Style.FILL

    &#125;

    override fun onSizeChanged(w: Int, h: Int, oldw: Int, oldh: Int) &#123;
        super.onSizeChanged(w, h, oldw, oldh)
        viewWidth = w
        mBgRect.set(0f, 0f, w * 1f, h * 1f)
        mRadius = h / 2f
    &#125;

    /**
     * 设置指示器背景进度条的颜色
     * @param color 背景色
     */
    fun setBgColor(@ColorInt color: Int) &#123;
        mBgPaint.color = color
        invalidate()
    &#125;

    /**
     * 设置指示器的颜色
     * @param color 指示器颜色
     */
    fun setIndicatorColor(@ColorInt color: Int) &#123;
        mPaint.color = color
        invalidate()
    &#125;

    /**
     * 绑定recyclerView
     */
    fun bindRecyclerView(recyclerView: RecyclerView) &#123;
        recyclerView.addOnScrollListener(object : RecyclerView.OnScrollListener() &#123;
            override fun onScrolled(recyclerView: RecyclerView, dx: Int, dy: Int) &#123;
                super.onScrolled(recyclerView, dx, dy)
                val offsetX = recyclerView.computeHorizontalScrollOffset() //已经向下滚动的距离，为0时表示已处于顶部。
                val range = recyclerView.computeHorizontalScrollRange()   //整体的高度，注意是整体，包括在显示区域之外的
                val extend = recyclerView.computeHorizontalScrollExtent() //当前RcyclerView显示区域的高度。水平列表屏幕从左侧到右侧显示范围
                val progress: Float = offsetX * 1.0f / (range - extend)
                this@HIndicator.progress = progress     //设置滚动距离所占比例

                Log.d("==distance==offsetX",offsetX.toString())
                Log.d("==distance==range",range.toString())
                Log.d("==distance==extend",extend.toString())
                Log.d("==distance==progress",progress.toString())


            &#125;
        &#125;)

        recyclerView.addOnLayoutChangeListener &#123; _, _, _, _, _, _, _, _, _ ->
            val range = recyclerView.computeHorizontalScrollRange()
            val extend = recyclerView.computeHorizontalScrollExtent()
            val ratio = extend * 1f / range
            this@HIndicator.ratio = ratio       //设置指示器所占的长度比例
        &#125;
    &#125;

    override fun onDraw(canvas: Canvas?) &#123;
        super.onDraw(canvas)
        //绘制背景
        canvas?.drawRoundRect(mBgRect, mRadius, mRadius, mBgPaint)

        //计算指示器的长度和位置
        val leftOffset = viewWidth * (1f - ratio) * progress
        val left = mBgRect.left + leftOffset
        val right = left + viewWidth * ratio
        mRect.set(left, mBgRect.top, right, mBgRect.bottom)

        //绘制指示器
        canvas?.drawRoundRect(mRect, mRadius, mRadius, mPaint)
    &#125;

&#125;
</code></pre>
<pre><code>class MainActivity : AppCompatActivity() &#123;

    override fun onCreate(savedInstanceState: Bundle?) &#123;
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        recyclerView.adapter = MAdapter()
        hIndicator.bindRecyclerView(recyclerView)


        btn1.setOnClickListener &#123;
            hIndicator.setBgColor(Color.parseColor("#333333"))
        &#125;


        btn2.setOnClickListener &#123;
            hIndicator.setIndicatorColor(Color.parseColor("#ffffff"))
        &#125;
    &#125;

    private inner class MAdapter : RecyclerView.Adapter<MViewHolder>() &#123;
        override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MViewHolder =
            MViewHolder(
                LayoutInflater.from(parent.context).inflate(
                    R.layout.item_test,
                    parent,
                    false
                )
            )


        override fun getItemCount(): Int = 15

        override fun onBindViewHolder(holder: MViewHolder, position: Int) &#123;
        &#125;

    &#125;

    private inner class MViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView)
&#125;



    <androidx.recyclerview.widget.RecyclerView
        android:id="@+id/recyclerView"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal"
        app:layoutManager="androidx.recyclerview.widget.GridLayoutManager"
        app:spanCount="2"/>

</code></pre>
  
</div>
            