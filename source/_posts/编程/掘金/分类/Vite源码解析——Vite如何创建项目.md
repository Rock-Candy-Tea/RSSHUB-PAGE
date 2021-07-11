
---
title: 'Vite源码解析——Vite如何创建项目'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ffa23c309d04127bc99c2af39bb7565~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 23:56:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ffa23c309d04127bc99c2af39bb7565~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:18px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:40px;margin-bottom:20px;color:#007fff;display:flex;align-items:center&#125;.markdown-body h1:hover:before,.markdown-body h2:hover:before,.markdown-body h3:hover:before,.markdown-body h4:hover:before,.markdown-body h5:hover:before,.markdown-body h6:hover:before&#123;transition:All .4s ease-in-out;transform:rotate(1turn)&#125;.markdown-body h1&#123;font-size:30px;background:linear-gradient(#fff 60%,#c6e3ff 0)&#125;.markdown-body h1:before&#123;content:"";display:inline-block;width:32px;height:32px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h2&#123;font-size:24px;background:linear-gradient(#fff 60%,#cce3fb 0)&#125;.markdown-body h2:before&#123;content:"";display:inline-block;width:24px;height:24px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h3&#123;font-size:20px&#125;.markdown-body h3:before&#123;content:"";display:inline-block;width:18px;height:18px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h4&#123;font-size:18px&#125;.markdown-body h4:before&#123;content:"";display:inline-block;width:16px;height:16px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h5&#123;font-size:16px&#125;.markdown-body h5:before&#123;content:"";display:inline-block;width:15px;height:15px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h6&#123;font-size:14px&#125;.markdown-body h6:before&#123;content:"";display:inline-block;width:12px;height:12px;margin-right:10px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC");background-size:100% 100%&#125;.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;border-bottom:2px solid #007fff;color:#007fff;padding-right:10px&#125;.markdown-body p&#123;letter-spacing:1px;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;display:block;max-width:100%;margin:10px auto&#125;.markdown-body hr&#123;border:none;border-top:1px dashed #92c8ff&#125;.markdown-body hr:before&#123;content:"✂";display:inline-block;position:relative;top:-12px;left:40px;padding:0 3px;color:#007fff;font-size:18px&#125;.markdown-body hr:after&#123;content:"按虚线剪开";position:relative;top:-15px;left:84%;padding:0 3px;color:#007fff;font-size:12px&#125;.markdown-body del&#123;color:#f44&#125;.markdown-body em&#123;color:#007fff;margin:0 2px&#125;.markdown-body strong&#123;color:#007fff;font-weight:bolder&#125;.markdown-body code&#123;word-break:break-word;border-radius:4px;overflow-x:auto;background-color:#e6f3ff;color:#007fff;font-weight:600;font-size:16px;padding:.065em .4em;border:1px solid #007fff&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:5px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:18px;font-weight:400;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8;border:none&#125;.markdown-body a&#123;text-decoration:none;color:#007fff;border-bottom:1px solid #007fff&#125;.markdown-body a:before&#123;content:"¶";margin-right:5px;font-size:22px&#125;.markdown-body a:after&#123;content:"↷";margin-left:2px;font-size:22px;display:none&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c;border-bottom:1px solid #275b8c&#125;.markdown-body a:active:after,.markdown-body a:hover:after&#123;display:inline-block&#125;.markdown-body table&#123;display:inline-block!important;font-size:16px;width:auto;max-width:100%;overflow:auto;border:1px solid #a5d3ff&#125;.markdown-body thead&#123;background:#c6e3ff;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#eef7ff&#125;.markdown-body tbody>tr:nth-child(odd)&#123;background-color:#f8fcff&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #007fff;background-color:#eef7ff&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol li::marker,.markdown-body ul li::marker&#123;color:#007fff&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>随着 Vite2 的发布并日趋稳定，现在越来越多的项目开始尝试使用它。我们使用 Vite 是一般会用下面这些命令去创建一个项目：</p>
<pre><code class="copyable">// 使用 npm
npm init @vitejs/app
// 使用 yarn
yarn create @vitejs/app

// 想指定项目名称和使用某个特定框架的模版时，可以像下面这样
// npm
npm init @vitejs/app my-vue-app --template vue
// yarn
yarn create @vitejs/app my-vue-app --template vue
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行这些命令后就会生成一个项目文件夹，对于大多数人可能觉得只要能正常创建一个项目就够了，但我出于好奇，为什么运行这些命令就会生成一个项目文件夹。这里以 yarn 为例创建项目进行说明。</p>
<h3 data-id="heading-1">yarn create 做了什么</h3>
<p>可能很多人会疑惑，为什么很多项目的创建方式都是使用<code>yarn create</code>这个命令进行创建。除了这里的 Vite，我们创建 React 项目也是这样：<code>yarn create react-app my-app</code>。</p>
<p>那这个命令到底做了什么，它其实做了两件事：</p>
<pre><code class="copyable">yarn global add create-react-app
create-react-app my-app
<span class="copy-code-btn">复制代码</span></code></pre>
<p>关于<code>yarn create</code>的更多内容可以看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwayou.github.io%2F2020%2F05%2F13%2F%25E5%2588%259B%25E5%25BB%25BA-Yarn-NPM-%25E8%2584%259A%25E6%2589%258B%25E6%259E%25B6%25E5%25BF%25AB%25E9%2580%259F%25E7%2594%259F%25E6%2588%2590%25E9%25A1%25B9%25E7%259B%25AE%2F%23%3A~%3Atext%3Dyarn%2520create%2520%253Cstarter-kit-package%253E%2520%255B%253Cargs%253E%255D%2520%25E6%2598%25AF%25E4%25B8%25BA%25E4%25BA%2586%25E7%25BB%259F%25E4%25B8%2580%25E5%2589%258D%25E7%25AB%25AF%25E9%25A1%25B9%25E7%259B%25AE%25E8%2584%259A%25E6%2589%258B%25E6%259E%25B6%25E5%25BC%2595%25E5%2585%25A5%25E7%259A%2584%25EF%25BC%258C%25E8%25BF%2599%25E4%25B9%258B%25E5%2589%258D%25EF%25BC%258C%25E5%2590%2584%25E9%25A1%25B9%25E7%259B%25AE%25E4%25BC%259A%25E6%259C%2589%25E8%2587%25AA%25E5%25B7%25B1%25E7%259A%2584%25E6%2596%25B9%25E5%25BC%258F%25E5%2592%258C%25E5%25A7%25BF%25E5%258A%25BF%25E6%259D%25A5%25E7%2594%259F%25E6%2588%2590%25E6%2596%25B0%25E9%25A1%25B9%25E7%259B%25AE%25E3%2580%2582%2520%25E8%25BF%2599%25E9%2587%258C%25EF%25BC%258C%25E7%25BA%25A6%25E5%25AE%259A%2520%253Cstarter-kit-package%253E%2520%25E4%25B8%25BA%2Ccreate-%2520%25E5%25BC%2580%25E5%25A4%25B4%25E7%259A%2584%2520npm%2520%25E5%258C%2585%25EF%25BC%258C%25E9%2580%259A%25E8%25BF%2587%2520package.json%2520bin%2520%25E5%25AD%2597%25E6%25AE%25B5%2520%25E5%25AF%25B9%25E5%25A4%2596%25E5%25AF%25BC%25E5%2587%25BA%25E5%258F%25AF%25E6%2589%25A7%25E8%25A1%258C%25E5%2591%25BD%25E4%25BB%25A4%25E7%2594%25A8%25E4%25BA%258E%25E5%2588%259B%25E5%25BB%25BA%25E6%2596%25B0%25E9%25A1%25B9%25E7%259B%25AE%25E6%2597%25B6%25E6%2589%25A7%25E8%25A1%258C%25E3%2580%2582" target="_blank" rel="nofollow noopener noreferrer" title="https://wayou.github.io/2020/05/13/%E5%88%9B%E5%BB%BA-Yarn-NPM-%E8%84%9A%E6%89%8B%E6%9E%B6%E5%BF%AB%E9%80%9F%E7%94%9F%E6%88%90%E9%A1%B9%E7%9B%AE/#:~:text=yarn%20create%20%3Cstarter-kit-package%3E%20%5B%3Cargs%3E%5D%20%E6%98%AF%E4%B8%BA%E4%BA%86%E7%BB%9F%E4%B8%80%E5%89%8D%E7%AB%AF%E9%A1%B9%E7%9B%AE%E8%84%9A%E6%89%8B%E6%9E%B6%E5%BC%95%E5%85%A5%E7%9A%84%EF%BC%8C%E8%BF%99%E4%B9%8B%E5%89%8D%EF%BC%8C%E5%90%84%E9%A1%B9%E7%9B%AE%E4%BC%9A%E6%9C%89%E8%87%AA%E5%B7%B1%E7%9A%84%E6%96%B9%E5%BC%8F%E5%92%8C%E5%A7%BF%E5%8A%BF%E6%9D%A5%E7%94%9F%E6%88%90%E6%96%B0%E9%A1%B9%E7%9B%AE%E3%80%82%20%E8%BF%99%E9%87%8C%EF%BC%8C%E7%BA%A6%E5%AE%9A%20%3Cstarter-kit-package%3E%20%E4%B8%BA,create-%20%E5%BC%80%E5%A4%B4%E7%9A%84%20npm%20%E5%8C%85%EF%BC%8C%E9%80%9A%E8%BF%87%20package.json%20bin%20%E5%AD%97%E6%AE%B5%20%E5%AF%B9%E5%A4%96%E5%AF%BC%E5%87%BA%E5%8F%AF%E6%89%A7%E8%A1%8C%E5%91%BD%E4%BB%A4%E7%94%A8%E4%BA%8E%E5%88%9B%E5%BB%BA%E6%96%B0%E9%A1%B9%E7%9B%AE%E6%97%B6%E6%89%A7%E8%A1%8C%E3%80%82" ref="nofollow noopener noreferrer">这里</a></p>
<h2 data-id="heading-2">源码解析</h2>
<p><code>yarn create @vitejs/app</code>命令运行后就会执行<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fvite%2Ftree%2Fmain%2Fpackages%2Fcreate-app" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/vite/tree/main/packages/create-app" ref="nofollow noopener noreferrer">@vitejs/create-app</a>里的代码。我们先看看这文件的项目结构</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ffa23c309d04127bc99c2af39bb7565~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-07-11 11.17.13.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>template 开头的文件夹都是各个框架和对应的typescript版本的项目模板，我们不用太关心，创建项目的逻辑都在 index.js 文件里。下面就来看看这里面都做了什么</p>
<h3 data-id="heading-3">项目依赖</h3>
<p>首先是依赖的引入</p>
<pre><code class="copyable">const fs = require('fs')
const path = require('path')
const argv = require('minimist')(process.argv.slice(2))
const prompts = require('prompts')
const &#123;
  yellow,
  green,
  cyan,
  blue,
  magenta,
  lightRed,
  red
&#125; = require('kolorist')
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>fs</code>、<code>path</code>是Nodejs内置模块，<code>minimist</code>、<code>prompts</code>、<code>kolorist</code>则分别是第三方依赖库。</p>
<ul>
<li>minimist：是一个用于解析命令行参数的工具。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fminimist" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/minimist" ref="nofollow noopener noreferrer">文档</a></li>
<li>prompts：是一个命令行交互的工具。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fprompts" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/prompts" ref="nofollow noopener noreferrer">文档</a></li>
<li>kolorist：是一个使命令行输出带有色彩的工具。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fkolorist" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/kolorist" ref="nofollow noopener noreferrer">文档</a></li>
</ul>
<h3 data-id="heading-4">模版配置</h3>
<p>接下来不同框架模版的配置文件，最后生成一个模版名称的数组。</p>
<pre><code class="copyable">// 这里只写了vue和react框架的配置，其他的都是差的不多，感兴趣可以去看源码。
const FRAMEWORKS = [
  ......
  
  &#123;
    name: 'vue',
    color: green,
    variants: [
      &#123;
        name: 'vue',
        display: 'JavaScript',
        color: yellow
      &#125;,
      &#123;
        name: 'vue-ts',
        display: 'TypeScript',
        color: blue
      &#125;
    ]
  &#125;,
  &#123;
    name: 'react',
    color: cyan,
    variants: [
      &#123;
        name: 'react',
        display: 'JavaScript',
        color: yellow
      &#125;,
      &#123;
        name: 'react-ts',
        display: 'TypeScript',
        color: blue
      &#125;
    ]
  &#125;,
  
  ......
]

// 输出模版名称列表
const TEMPLATES = FRAMEWORKS.map(
  (f) => (f.variants && f.variants.map((v) => v.name)) || [f.name]
).reduce((a, b) => a.concat(b), [])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其次，由于 .gitignore 文件的特殊性，每种框架项目模版下都是先创建的 _gitignore 文件，在后续创建项目的时候再替换为 .gitignore。所以，代码里会预先定义一个对象来存放需要重命名的文件：</p>
<pre><code class="copyable">const renameFiles = &#123;
  _gitignore: '.gitignore'
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">工具函数</h3>
<p>在开始讲的核心函数之前，先来看看代码中定义的工具函数。最重要的是与文件操作相关的三个函数。</p>
<h4 data-id="heading-6">copy</h4>
<pre><code class="copyable">function copy(src, dest) &#123;
  const stat = fs.statSync(src)
  if (stat.isDirectory()) &#123;
    copyDir(src, dest)
  &#125; else &#123;
    fs.copyFileSync(src, dest)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>copy</code>函数则用于复制文件或文件夹 src 到指定文件夹 dest。它会先获取 src 的状态 stat，如果 src 是文件夹的话，即<code>stat.isDirectory()</code>为 true 时，则会调用下面将介绍的<code>copyDir</code>函数来复制 src 文件夹下的文件到 dest 文件夹下。反之，src 是文件的话，则直接调用 fs.copyFileSync 函数复制 src 文件到 dest 文件夹下。</p>
<h4 data-id="heading-7">copyDir</h4>
<pre><code class="copyable">function copyDir(srcDir, destDir) &#123;
  fs.mkdirSync(destDir, &#123; recursive: true &#125;)
  for (const file of fs.readdirSync(srcDir)) &#123;
    const srcFile = path.resolve(srcDir, file)
    const destFile = path.resolve(destDir, file)
    copy(srcFile, destFile)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>copyDir</code>函数用于将某个文件夹 srcDir 中的文件复制到指定文件夹 destDir 中。它会先调用 <code>fs.mkdirSync</code>函数来创建制定的文件夹，然后调用<code>fs.readdirSync</code>从 srcDir 文件夹下获取的文件并遍历逐个复制；最后在调用<code>copy</code>函数进行复制，这里用到了递归，因为可能存在文件夹里的文件还是文件夹。</p>
<h4 data-id="heading-8">emptyDir</h4>
<pre><code class="copyable">function emptyDir(dir) &#123;
  if (!fs.existsSync(dir)) &#123;
    return
  &#125;
  for (const file of fs.readdirSync(dir)) &#123;
    const abs = path.resolve(dir, file)
    if (fs.lstatSync(abs).isDirectory()) &#123;
      emptyDir(abs)
      fs.rmdirSync(abs)
    &#125; else &#123;
      fs.unlinkSync(abs)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>emptyDir</code>函数用于清空 dir 文件夹下的代码。它会先判断 dir 文件夹是否存在，存在则遍历该问文件夹下的文件，构造该文件的路径 abs，当 abs 为文件夹时，会递归调用 emptyDir 函数删除该文件夹下的文件，然后再调用<code>fs.rmdirSync</code>删除该文件夹；当 abs 是文件时，则调用<code>fs.unlinkSync</code>函数来删除该文件。</p>
<h3 data-id="heading-9">核心函数</h3>
<p>接下来就是核心功能实现的<code>init</code>函数。</p>
<h4 data-id="heading-10">命令行交互并创建文件夹</h4>
<p>首先是获取命令行参数</p>
<pre><code class="copyable">let targetDir = argv._[0]
let template = argv.template || argv.t

const defaultProjectName = !targetDir ? 'vite-project' : targetDir
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>argv._[0]</code> 代表 <code>@vitejs/app</code> 后的第一个参数</p>
<p><code>template</code>则是要使用的模版名称</p>
<p><code>defaultProjectName</code>则是我们创建的项目名称。</p>
<p>接下来就是使用<code>prompts</code>包来在命令行中输出询问，像下面这样：
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd0a0477c8fc44baa31751bc909ed5db~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-07-11 14.53.38.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>具体代码如下：</p>
<pre><code class="copyable">// 关于命令行交互的部分代码没有全部放在这里，感兴趣的可以去看源码
let result = &#123;&#125;

result = await prompts(
  [
    &#123;
      type: targetDir ? null : 'text',
      name: 'projectName',
      message: 'Project name:',
      initial: defaultProjectName,
      onState: (state) =>
        (targetDir = state.value.trim() || defaultProjectName)
    &#125;,
    ......
    
  ]
)

const &#123; framework, overwrite, packageName, variant &#125; = result

const root = path.join(cwd, targetDir)

if (overwrite) &#123;
  emptyDir(root)
&#125; else if (!fs.existsSync(root)) &#123;
  fs.mkdirSync(root)
&#125;

template = variant || framework || template

// 输出项目文件夹路径
console.log(`\nScaffolding project in $&#123;root&#125;...`)

const templateDir = path.join(__dirname, `template-$&#123;template&#125;`)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>选择完成后会返回我们选择的结果<code>result</code></p>
<p><code>root</code>是通过<code>path.join</code>函数构建的完整文件路径</p>
<p><code>overwrite</code>是针对已存在我们要创建的同名文件时，是否要重写，如果重写，则调用前面的<code>emptyDir</code>函数清空该文件夹，如果不存在该文件夹，则调用<code>fs.mkdirSync</code>创建文件夹</p>
<p><code>templateDir</code>选择的模版文件夹名称</p>
<h4 data-id="heading-11">写入文件</h4>
<pre><code class="copyable">const write = (file, content) => &#123;
  const targetPath = renameFiles[file]
    ? path.join(root, renameFiles[file])
    : path.join(root, file)
  if (content) &#123;
    fs.writeFileSync(targetPath, content)
  &#125; else &#123;
      copy(path.join(templateDir, file), targetPath)
  &#125;
&#125;

const files = fs.readdirSync(templateDir)
for (const file of files.filter((f) => f !== 'package.json')) &#123;
  write(file)
&#125;

const pkg = require(path.join(templateDir, `package.json`))

pkg.name = packageName

write('package.json', JSON.stringify(pkg, null, 2))

const pkgManager = /yarn/.test(process.env.npm_execpath) ? 'yarn' : 'npm'

// 输出一些提示告诉你项目已经创建结束，以及告诉你接下来启动项目需要运行的命令
console.log(`\nDone. Now run:\n`)
if (root !== cwd) &#123;
console.log(`  cd $&#123;path.relative(cwd, root)&#125;`)
&#125;
console.log(`  $&#123;pkgManager === 'yarn' ? `yarn` : `npm install`&#125;`)
console.log(`  $&#123;pkgManager === 'yarn' ? `yarn dev` : `npm run dev`&#125;`)
console.log()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>write</code>函数则接受两个参数 file 和 content，它有两个功能：</p>
<ul>
<li>对指定的文件 file 写入指定的内容 content，调用<code>fs.writeFileSync</code>函数来实现将内容写入文件。</li>
<li>复制模版文件夹下的文件到指定文件夹下，调用前面介绍的<code>copy</code>函数来实现文件的复制。</li>
</ul>
<p>然后调用<code>fs.readdirSync</code>读取模版文件夹里的文件，遍历逐一复制到项目文件夹（其中要过滤的 package.json 文件，因为其中的 name 字段要修改）；最后再写入 package.json 文件。</p>
<h2 data-id="heading-12">小结</h2>
<p>Vite 的<code>create-app</code>包的实现只有320行左右的代码，但它考虑到各种场景的兼容处理；在学习完之后，自己去实现一个这样的CLI工具也不是什么难事。</p></div>  
</div>
            