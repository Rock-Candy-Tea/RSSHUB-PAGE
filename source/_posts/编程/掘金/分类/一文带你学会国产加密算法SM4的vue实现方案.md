
---
title: '一文带你学会国产加密算法SM4的vue实现方案'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97a2514f16764bd181d7b359eed733d4~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 04 Jun 2021 04:42:10 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97a2514f16764bd181d7b359eed733d4~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第4天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h3 data-id="heading-0">前言</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97a2514f16764bd181d7b359eed733d4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><br>
说起前端的vue，真的是一个非常好用的框架，vue也是现在web项目的主流前端开发方案。所以基于vue的sm4加密实现方案是十分有必要掌握的。</p>
<h3 data-id="heading-1">国产SM4加密解密算法概念介绍</h3>
<p>SMS4算法是在国内广泛使用的WAPI无线网络标准中使用的加密算法，是一种32轮的迭代非平衡Feistel结构的分组加密算法，其密钥长度和分组长度均为128。SMS4算法的加解密过程中使用的算法是完全相同的，唯一不同点在于该算法的解密密钥是由它的加密密钥进行逆序变换后得到的。<br>
SMS4分组加密算法是中国无线标准中使用的分组加密算法，在2012年已经被国家商用密码管理局确定为国家密码行业标准，标准编号GM/T 0002-2012并且改名为SM4算法，与SM2椭圆曲线公钥密码算法，SM3密码杂凑算法共同作为国家密码的行业标准，在我国密码行业中有着极其重要的位置。<br>
SMS4算法的分组长度为128bit，密钥长度也是128bit。加解密算法均采用32轮非平衡Feistel迭代结构，该结构最先出现在分组密码LOKI的密钥扩展算法中。SMS4通过32轮非线性迭代后加上一个反序变换，这样只需要解密密钥是加密密钥的逆序，就能使得解密算法与加密算法保持一致。SMS4加解密算法的结构完全相同，只是在使用轮密钥时解密密钥是加密密钥的逆序。<br>
S盒是一种利用非线性变换构造的分组密码的一个组件，主要是为了实现分组密码过程中的混淆的特性和设计的。SMS4算法中的S盒在设计之初完全按照欧美分组密码的设计标准进行，它采用的方法是能够很好抵抗差值攻击的仿射函数逆映射复合法。</p>
<h3 data-id="heading-2">SM4加密算法应用场景</h3>
<p>SM4常用于政府系统的数据传输加密，比如当我们前端向后台传参数的时候，可以使用此算法。对参数的数据进行加密，然后后台对加密的数据进行解密再存储到数据库中，保证数据传输过程中，不受泄露。<br>
本次提供的方案不仅提供sm4的加密解密，还提供了md5算法的完整性防篡改校验。</p>
<h3 data-id="heading-3">vue的加密方案实现流程</h3>
<p>针对于我们的前端vue来说，我们通过axios来进行请求和响应，在我们vue的项目中，必然有一个request.js文件，用于封装request和respone。那么我们通过sm4的工具类。拦截所有的request请求进行加密，使用md5对参数进行加密，作为参数的一种防篡改表示，放在request的请求头中，供后台进行校验。在我们response的时候，同样进行拦截回应，将回应的数据的加密值进行解析。并使用md5重新加密，使我们获得的数据防篡改。</p>
<h3 data-id="heading-4">基于vue的sm4加密解密工具</h3>
<p>我们先介绍一下vue的加密解密工具类。通过调用工具类的方法可以直接对数据进行加密解密，配合request和response即可实现。我们贴出下面的工具类代码，大家可以直接使用。</p>
<pre><code class="copyable">const SboxTable = [
  [0xd6, 0x90, 0xe9, 0xfe, 0xcc, 0xe1, 0x3d, 0xb7, 0x16, 0xb6, 0x14, 0xc2, 0x28, 0xfb, 0x2c, 0x05],
  [0x2b, 0x67, 0x9a, 0x76, 0x2a, 0xbe, 0x04, 0xc3, 0xaa, 0x44, 0x13, 0x26, 0x49, 0x86, 0x06, 0x99],
  [0x9c, 0x42, 0x50, 0xf4, 0x91, 0xef, 0x98, 0x7a, 0x33, 0x54, 0x0b, 0x43, 0xed, 0xcf, 0xac, 0x62],
  [0xe4, 0xb3, 0x1c, 0xa9, 0xc9, 0x08, 0xe8, 0x95, 0x80, 0xdf, 0x94, 0xfa, 0x75, 0x8f, 0x3f, 0xa6],
  [0x47, 0x07, 0xa7, 0xfc, 0xf3, 0x73, 0x17, 0xba, 0x83, 0x59, 0x3c, 0x19, 0xe6, 0x85, 0x4f, 0xa8],
  [0x68, 0x6b, 0x81, 0xb2, 0x71, 0x64, 0xda, 0x8b, 0xf8, 0xeb, 0x0f, 0x4b, 0x70, 0x56, 0x9d, 0x35],
  [0x1e, 0x24, 0x0e, 0x5e, 0x63, 0x58, 0xd1, 0xa2, 0x25, 0x22, 0x7c, 0x3b, 0x01, 0x21, 0x78, 0x87],
  [0xd4, 0x00, 0x46, 0x57, 0x9f, 0xd3, 0x27, 0x52, 0x4c, 0x36, 0x02, 0xe7, 0xa0, 0xc4, 0xc8, 0x9e],
  [0xea, 0xbf, 0x8a, 0xd2, 0x40, 0xc7, 0x38, 0xb5, 0xa3, 0xf7, 0xf2, 0xce, 0xf9, 0x61, 0x15, 0xa1],
  [0xe0, 0xae, 0x5d, 0xa4, 0x9b, 0x34, 0x1a, 0x55, 0xad, 0x93, 0x32, 0x30, 0xf5, 0x8c, 0xb1, 0xe3],
  [0x1d, 0xf6, 0xe2, 0x2e, 0x82, 0x66, 0xca, 0x60, 0xc0, 0x29, 0x23, 0xab, 0x0d, 0x53, 0x4e, 0x6f],
  [0xd5, 0xdb, 0x37, 0x45, 0xde, 0xfd, 0x8e, 0x2f, 0x03, 0xff, 0x6a, 0x72, 0x6d, 0x6c, 0x5b, 0x51],
  [0x8d, 0x1b, 0xaf, 0x92, 0xbb, 0xdd, 0xbc, 0x7f, 0x11, 0xd9, 0x5c, 0x41, 0x1f, 0x10, 0x5a, 0xd8],
  [0x0a, 0xc1, 0x31, 0x88, 0xa5, 0xcd, 0x7b, 0xbd, 0x2d, 0x74, 0xd0, 0x12, 0xb8, 0xe5, 0xb4, 0xb0],
  [0x89, 0x69, 0x97, 0x4a, 0x0c, 0x96, 0x77, 0x7e, 0x65, 0xb9, 0xf1, 0x09, 0xc5, 0x6e, 0xc6, 0x84],
  [0x18, 0xf0, 0x7d, 0xec, 0x3a, 0xdc, 0x4d, 0x20, 0x79, 0xee, 0x5f, 0x3e, 0xd7, 0xcb, 0x39, 0x48],
];

const FK = [0xa3b1bac6, 0x56aa3350, 0x677d9197, 0xb27022dc];
const CK = [
  0x00070e15, 0x1c232a31, 0x383f464d, 0x545b6269,
  0x70777e85, 0x8c939aa1, 0xa8afb6bd, 0xc4cbd2d9,
  0xe0e7eef5, 0xfc030a11, 0x181f262d, 0x343b4249,
  0x50575e65, 0x6c737a81, 0x888f969d, 0xa4abb2b9,
  0xc0c7ced5, 0xdce3eaf1, 0xf8ff060d, 0x141b2229,
  0x30373e45, 0x4c535a61, 0x686f767d, 0x848b9299,
  0xa0a7aeb5, 0xbcc3cad1, 0xd8dfe6ed, 0xf4fb0209,
  0x10171e25, 0x2c333a41, 0x484f565d, 0x646b7279,
];

const SM4_ENCRYPT = 1;
const SM4_DECRYPT = 0;

function sm4_context() &#123;
  this.mode = 0;
  this.sk = [];
&#125;


function GET_ULONG_BE(n, b, i) &#123;
  return (b[i] << 24) | (b[i + 1] << 16) | (b[i + 2]) << 8 | (b[i + 3]);
&#125;

function PUT_ULONG_BE(n, b, i) &#123;
  b[i] = n >>> 24;
  b[i + 1] = n >>> 16;
  b[i + 2] = n >>> 8;
  b[i + 3] = n;
&#125;

function ROTL(x, n) &#123;
  const a = (x & 0xFFFFFFFF) << n;
  const b = x >>> (32 - n);

  return a | b;
&#125;


function sm4Sbox(n) &#123;
  const l = n >>> 4;
  const r = n % 16;
  return SboxTable[l][r];
&#125;

function sm4Lt(ka) &#123;
  let bb = 0;
  let c = 0;
  const a = new Uint8Array(4);
  const b = new Array(4);
  PUT_ULONG_BE(ka, a, 0);
  b[0] = sm4Sbox(a[0]);
  b[1] = sm4Sbox(a[1]);
  b[2] = sm4Sbox(a[2]);
  b[3] = sm4Sbox(a[3]);
  bb = GET_ULONG_BE(bb, b, 0);

  c = bb ^ (ROTL(bb, 2)) ^ (ROTL(bb, 10)) ^ (ROTL(bb, 18)) ^ (ROTL(bb, 24));
  return c;
&#125;

function sm4F(x0, x1, x2, x3, rk) &#123;
  return (x0 ^ sm4Lt(x1 ^ x2 ^ x3 ^ rk));
&#125;

function sm4CalciRK(ka) &#123;
  let bb = 0;
  let rk = 0;
  const a = new Uint8Array(4);
  const b = new Array(4);
  PUT_ULONG_BE(ka, a, 0);
  b[0] = sm4Sbox(a[0]);
  b[1] = sm4Sbox(a[1]);
  b[2] = sm4Sbox(a[2]);
  b[3] = sm4Sbox(a[3]);
  bb = GET_ULONG_BE(bb, b, 0);

  rk = bb ^ (ROTL(bb, 13)) ^ (ROTL(bb, 23));

  return rk;
&#125;

function sm4_setkey(SK, key) &#123;
  const MK = new Array(4);
  const k = new Array(36);
  let i = 0;
  MK[0] = GET_ULONG_BE(MK[0], key, 0);
  MK[1] = GET_ULONG_BE(MK[1], key, 4);
  MK[2] = GET_ULONG_BE(MK[2], key, 8);
  MK[3] = GET_ULONG_BE(MK[3], key, 12);

  k[0] = MK[0] ^ FK[0];
  k[1] = MK[1] ^ FK[1];
  k[2] = MK[2] ^ FK[2];
  k[3] = MK[3] ^ FK[3];

  for (; i < 32; i++) &#123;
    k[i + 4] = k[i] ^ (sm4CalciRK(k[i + 1] ^ k[i + 2] ^ k[i + 3] ^ CK[i]));
    SK[i] = k[i + 4];
  &#125;
&#125;

function sm4_one_round(sk, input, output) &#123;
  let i = 0;
  const ulbuf = new Array(36);

  ulbuf[0] = GET_ULONG_BE(ulbuf[0], input, 0);
  ulbuf[1] = GET_ULONG_BE(ulbuf[1], input, 4);
  ulbuf[2] = GET_ULONG_BE(ulbuf[2], input, 8);
  ulbuf[3] = GET_ULONG_BE(ulbuf[3], input, 12);
  while (i < 32) &#123;
    ulbuf[i + 4] = sm4F(ulbuf[i], ulbuf[i + 1], ulbuf[i + 2], ulbuf[i + 3], sk[i]);
    i++;
  &#125;

  PUT_ULONG_BE(ulbuf[35], output, 0);
  PUT_ULONG_BE(ulbuf[34], output, 4);
  PUT_ULONG_BE(ulbuf[33], output, 8);
  PUT_ULONG_BE(ulbuf[32], output, 12);
&#125;

function sm4_setkey_enc(ctx, key) &#123;
  ctx.mode = SM4_ENCRYPT;
  sm4_setkey(ctx.sk, key);
&#125;

function sm4_setkey_dec(ctx, key) &#123;
  let i; let j;
  ctx.mode = SM4_ENCRYPT;
  sm4_setkey(ctx.sk, key);
  for (i = 0; i < 16; i++) &#123;
    j = ctx.sk[31 - i];
    ctx.sk[31 - i] = ctx.sk[i];
    ctx.sk[i] = j;
  &#125;
&#125;

function sm4_crypt_ecb(ctx, mode, length, input, output) &#123;
  let index = 0;
  while (length > 0) &#123;
    const oneInput = input.slice(index, index + 16);
    const oneOutput = new Uint8Array(16);
    sm4_one_round(ctx.sk, oneInput, oneOutput);

    for (let i = 0; i < 16; i++) &#123;
      output[index + i] = oneOutput[i];
    &#125;
    index += 16;
    length -= 16;
  &#125;
&#125;

function sm4_crypt_cbc(ctx, mode, length, iv, input, output) &#123;
  let i;
  const temp = new Array(16);
  let index = 0;

  if (mode == SM4_ENCRYPT) &#123;
    while (length > 0) &#123;
      const oneInput = input.slice(index, index + 16);
      const oneOutput = new Array(16);
      for (i = 0; i < 16; i++) &#123;
        oneOutput[i] = oneInput[i] ^ iv[i];
      &#125;

      sm4_one_round(ctx.sk, oneOutput, oneOutput);

      for (i = 0; i < 16; i++) &#123;
        iv[i] = oneOutput[i];
        output[index + i] = oneOutput[i];
      &#125;

      index += 16;
      length -= 16;
    &#125;
  &#125; else /* SM4_DECRYPT */ &#123;
    while (length > 0) &#123;
      const oneInput = input.slice(index, index + 16);
      const oneOutput = new Array(16);
      index += 16;
      for (i = 0; i < 16; i++) &#123;
        temp[i] = oneInput[i];
      &#125;

      sm4_one_round(ctx.sk, oneInput, oneOutput);

      for (i = 0; i < 16; i++) &#123;
        oneOutput[i] = oneOutput[i] ^ iv[i];
        output[index + i] = oneOutput[i];
      &#125;

      for (i = 0; i < 16; i++) &#123;
        iv[i] = temp[i];
      &#125;

      index += 16;
      length -= 16;
    &#125;
  &#125;
&#125;

function strfix(str, len) &#123;
  let length = len - str.length;
  while (length-- > 0) &#123;
    str = `0$&#123;str&#125;`;
  &#125;
  return str;
&#125;

function HEXStrXOR(str1, str2) &#123;
  const buf1 = hex2Array(str1);
  const buf2 = hex2Array(str2);

  let result = '';
  for (let i = 0; i < 16; i++) &#123;
    result += strfix((buf1[i] ^ buf2[i]).toString(16).toUpperCase(), 2);
  &#125;

  return result;
&#125;

function hex2Array(str) &#123;
  const len = str.length / 2;
  let substr = '';
  const result = new Array(len);
  for (let i = 0; i < len; i++) &#123;
    substr = str.slice(2 * i, 2 * (i + 1));
    result[i] = parseInt(substr, 16) || 0;
  &#125;
  return result;
&#125;


const stringToByteArray = function (str) &#123;
  const bytes = new Array();
  let len; let c;
  len = str.length;
  for (let i = 0; i < len; i++) &#123;
    c = str.charCodeAt(i);
    if (c >= 0x010000 && c <= 0x10FFFF) &#123;
      bytes.push(((c >> 18) & 0x07) | 0xF0);
      bytes.push(((c >> 12) & 0x3F) | 0x80);
      bytes.push(((c >> 6) & 0x3F) | 0x80);
      bytes.push((c & 0x3F) | 0x80);
    &#125; else if (c >= 0x000800 && c <= 0x00FFFF) &#123;
      bytes.push(((c >> 12) & 0x0F) | 0xE0);
      bytes.push(((c >> 6) & 0x3F) | 0x80);
      bytes.push((c & 0x3F) | 0x80);
    &#125; else if (c >= 0x000080 && c <= 0x0007FF) &#123;
      bytes.push(((c >> 6) & 0x1F) | 0xC0);
      bytes.push((c & 0x3F) | 0x80);
    &#125; else &#123;
      bytes.push(c & 0xFF);
    &#125;
  &#125;
  return bytes;
&#125;;

const hexStringToByteArray = function (str) &#123;
  let pos = 0;
  let len = str.length;
  if (len % 2 !== 0) &#123;
    return str;
  &#125;
  len /= 2;
  const arrBytes = new Array();
  for (let i = 0; i < len; i++) &#123;
    const s = str.substr(pos, 2);
    const v = parseInt(s, 16);
    arrBytes.push(v);
    pos += 2;
  &#125;
  return arrBytes;
&#125;;
const byteArrayToHexString = function (arr) &#123;
  let str = '';
  for (let i = 0; i < arr.length; i++) &#123;
    let tmp = arr[i].toString(16);
    if (tmp.length == 1) &#123;
      tmp = `0$&#123;tmp&#125;`;
    &#125;
    str += tmp;
  &#125;
  return str;
&#125;;
const byteArrayToString = function (arr) &#123;
  if (typeof arr === 'string') &#123;
    return arr;
  &#125;
  let str = '';
  const _arr = arr;
  for (let i = 0; i < _arr.length; i++) &#123;
    const one = _arr[i].toString(2);
    const v = one.match(/^1+?(?=0)/);
    if (v && one.length == 8) &#123;
      const bytesLength = v[0].length;
      let store = _arr[i].toString(2).slice(7 - bytesLength);
      for (let st = 1; st < bytesLength; st++) &#123;
        store += _arr[st + i].toString(2).slice(2);
      &#125;
      str += String.fromCharCode(parseInt(store, 2));
      i += bytesLength - 1;
    &#125; else &#123;
      str += String.fromCharCode(_arr[i]);
    &#125;
  &#125;
  return str;
&#125;;

function SM4CryptECBWithPKCS7Padding(data, sCryptFlag) &#123;
  const szSM4Key = 'cc9368581322479ebf3e79348a2757d9';
  if (szSM4Key.length !== 32) &#123;
    // console.log("传入密钥[" + szSM4Key + "]长度不为32位");
    return '';
  &#125;
  let szData = null;
  if (sCryptFlag === SM4_ENCRYPT) &#123; // 加密
    szData = stringToByteArray(data);
  &#125; else &#123; // 解密
    szData = hexStringToByteArray(data);
  &#125;
  const len = szData.length;

  if (sCryptFlag === SM4_ENCRYPT) &#123; // 加密,进行填充PKCS7Padding
    const p = 16 - len % 16;
    for (let i = 0; i < p; i++) &#123;
      szData.push(p);
    &#125;
  &#125;

  const ctx = new sm4_context();
  const lpbKey = hex2Array(szSM4Key);
  if (sCryptFlag === SM4_ENCRYPT) &#123;
    sm4_setkey_enc(ctx, lpbKey); // 加密
  &#125; else &#123;
    sm4_setkey_dec(ctx, lpbKey); // 解密
  &#125;
  const pbyCryptResult = new Array(szData.length);
  sm4_crypt_ecb(ctx, sCryptFlag, szData.length, szData, pbyCryptResult);
  if (sCryptFlag === SM4_DECRYPT) &#123; // 解密,去除填充PKCS7Padding
    const p = pbyCryptResult[pbyCryptResult.length - 1];
    for (let i = 0; i < p; i++) &#123;
      pbyCryptResult.pop();
    &#125;
  &#125;
  if (sCryptFlag === SM4_ENCRYPT) &#123; // 加密
    return byteArrayToHexString(pbyCryptResult);
  &#125; // 解密
  return byteArrayToString(pbyCryptResult);
&#125;

export function encrypt(inArray) &#123;
  return SM4CryptECBWithPKCS7Padding(inArray, 1);
&#125;

export function decrypt(inArray) &#123;
  return SM4CryptECBWithPKCS7Padding(inArray, 0);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上就是我们sm4的加密解密算法。其中重要的方法就是SM4CryptECBWithPKCS7Padding，这里我们要传入两个值，第一个值是我们加密或者要解密的值，第二个是标志是加密还是解密。当为1的时候，就是加密，当为0的时候就是解密。<br>
下面介绍一下md5加密的防篡改算法。</p>
<h3 data-id="heading-5">md5的加密算法</h3>
<p>md5加密我们直接采用模块crypto，针对于我们的vue项目，我们先将这个module进行安装。</p>
<pre><code class="copyable">cnpm install crypto
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装完成后，在我们需要进行md5加密的位置，进行加密，我们在这里是在request中进行加密。下面介绍一下md5加密的使用方式。</p>
<pre><code class="copyable">import crypto from 'crypto';

const md5Hash = crypto.createHash('md5');
const dataJson = JSON.stringify(data);
md5Hash.update(dataJson);
md5Data = md5Hash.digest('hex');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上我们就得到了参数的md5值。在对于后端的时候，要注意一个大坑，前端的这种加密方式，如果开头为0，并不会省略，如果后台使用bigInteger的方式，会导致后端的0直接被省略。导致md5值不一样，所以后端的md5校验推荐使用Integer的形式。<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6ac5235a31c4c22a9fa5524ff758c48~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">public class Md5Utils &#123;

    public static String getMD5String(String str) &#123;
        try &#123;
            MessageDigest md = MessageDigest.getInstance("md5");
            md.update(str.getBytes());
            byte s[] = md.digest();
            String result = "";
            for (int i = 0; i < s.length; i++) &#123;
                result += Integer.toHexString((0x000000FF & s[i]) | 0xFFFFFF00).substring(6);
            &#125;
            return result;
        &#125; catch (Exception e) &#123;
            e.printStackTrace();
            return null;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">基于vue的实例实战代码</h3>
<h4 data-id="heading-7">全局变量的配置和需要加密的url</h4>
<p>我们定义这样的两个变量。全局变量用于是否进行加密1是进行加密，0是进行解密。<br>
在encryptUrl 中key值配置为要加密的url，value值设置成属性必须加密name属性，sex属性不加密。</p>
<pre><code class="copyable">const isEncrypt = '1'; // 1是加密 0是不加密
// 将所有要加密的url和key放在一起
const encryptUrl = &#123;
  [/test/save`]: ['name'],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">针对于加密解密进行函数的封装</h4>
<p>上面已经有了可以使用的工具类，我们对此进行递归的函数封装。</p>
<pre><code class="copyable">function encryptValue(pObj, pParamKeys, pDecrypt) &#123;
  if (pObj) &#123;
    if (Array.isArray(pObj)) &#123;
      let i = pObj.length;
      while (i--) &#123;
        encryptValue(pObj[i], pParamKeys, pDecrypt);
      &#125;
    &#125; else if (typeof (pObj) === 'object') &#123;
      if (pObj.constructor !== RegExp) &#123;
        for (const k in pObj) &#123;
          if (pObj.hasOwnProperty(k)) &#123;
            if (typeof (pObj[k]) === 'object') &#123;
              encryptValue(pObj[k], pParamKeys, pDecrypt);
            &#125; else if (pParamKeys.indexOf(k) !== -1 && pObj[k]) &#123;
              if (pDecrypt === true) &#123;
                // 解密
                pObj[k] = decrypt(pObj[k]);
              &#125; else &#123;
                pObj[k] = encrypt(pObj[k]);
              &#125;
            &#125;
          &#125;
        &#125;
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">request的拦截方式</h4>
<p>我们首先拦截所有请求的request的地方，进行sm4加密解密。代码如下：</p>
<pre><code class="copyable">axios.interceptors.request.use(
  (config) => &#123;
    // 加密代码开始-------------------
    // 获取到当前请求的所有值
    const paramData = lodash.cloneDeep(config.data);
    // 获取到加密的url
    const urlAddr = config.url;
    let md5Data = '';
    if (paramData && isEncrypt === '1') &#123;
      let paramKeys = [];
      for (const key in encryptUrl) &#123;
        if (encryptUrl.hasOwnProperty(key)) &#123;
          if (urlAddr && urlAddr.startsWith(key)) &#123;
            paramKeys = encryptUrl[key];
            break;
          &#125;
        &#125;
      &#125;
      // 获取到所有要加密的key值。
      if (paramKeys && paramKeys.length > 0) &#123;
        let SM4cloneData = paramData;
        if (typeof (SM4cloneData) === 'string') &#123;
          try &#123;
            const dataStr = $.parseJSON(SM4cloneData);
            encryptValue(dataStr, paramKeys);
            SM4cloneData = JSON.stringify(dataStr);
          &#125; catch (e) &#123;
            console.log(e);
          &#125;
        &#125; else &#123;
          encryptValue(SM4cloneData, paramKeys);
        &#125;
      &#125;
      const md5Hash = crypto.createHash('md5');
      const dataJson = JSON.stringify(config.data);
      md5Hash.update(dataJson);
      md5Data = md5Hash.digest('hex');
      config.data = paramData;
    &#125;
      config.headers = &#123;
        'md5': md5Data,
      &#125;;
    return config;
  &#125;
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">response的拦截方式</h4>
<p>针对于response我们要对配置的url进行解密。</p>
<pre><code class="copyable">axios.interceptors.response.use(
  (response) => &#123;
    // 开始解密
    // 获取到当前请求的所有值
    const cloneData = lodash.cloneDeep(response.data);
    // 获取到解密的url
    const urlAddr = response.url;
    // 对paramData进行加密,此时先直接加密做试验。
    if (cloneData && isEncrypt === '1') &#123;
      let paramKeys = [];
      for (const key in encryptUrl) &#123;
        if (encryptUrl.hasOwnProperty(key)) &#123;
          if (urlAddr && urlAddr.startsWith(key)) &#123;
            paramKeys = encryptUrl[key];
            break;
          &#125;
        &#125;
      &#125;
      // 获取到所有要解密的key值。
      if (paramKeys && paramKeys.length > 0) &#123;
        let SM4cloneData;
        if (Array.isArray(cloneData)) &#123;
          SM4cloneData = cloneData.data;
        &#125; else if (typeof (cloneData) === 'object') &#123;
          SM4cloneData = cloneData;
        &#125;

        if (typeof (SM4cloneData) === 'string') &#123;
          try &#123;
            const dataStr = $.parseJSON(SM4cloneData);
            encryptValue(dataStr, paramKeys, true);
            SM4cloneData = JSON.stringify(dataStr);
          &#125; catch (e) &#123;
            console.log(e);
          &#125;
        &#125; else &#123;
          encryptValue(SM4cloneData, paramKeys, true);
        &#125;
        const md5Hash = crypto.createHash('md5');
        const dataJson = JSON.stringify(cloneData);
        md5Hash.update(dataJson);
        const md5Data = md5Hash.digest('hex');
        if (response.headers.md5.hasOwnProperty('md5')) &#123;
          if (md5Data === response.headers.md5) &#123;
            alert("md5完整性校验错误");
            return;
          &#125;
        &#125;
      &#125;
      return response.data;
    &#125;

    return response.data;
  &#125;,
  
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">总结</h3>
<p>支持基于vue的国产sm4加密解密方案到此结束。文中难免有不足之处，希望大家批评指正。<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50f99473ff724d0c80b975f6b7487827~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            