from rest_framework import renderers


class APIJSONRenderer(renderers.JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        success = False
        code = renderer_context["response"].status_code
        message = None
        if renderer_context:
            # 响应的信息，成功和错误的都是这个
            if renderer_context['response'].exception:
                # 响应信息中有message和code这两个key，则获取响应信息中的message和code，并且将原本data中的这两个key删除，放在自定义响应信息里
                # 响应信息中没有则将msg内容改为请求成功 code改为请求的状态码
                message = data.pop('detail', '失败')
                code = data.pop('code', renderer_context["response"].status_code)
            else:
                success = True

            # 自定义返回的格式
            ret = {
                'success': success,
                'code': code,
                'message': message,
                'data': data,
            }
            # 返回JSON数据
            return super().render(ret, accepted_media_type, renderer_context)
        else:
            return super().render(data, accepted_media_type, renderer_context)
