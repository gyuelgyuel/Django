## 외부라이브러리 사용

외부라이브러리 사용시 `pip install <library_name>`을 통해 설치를 해준 뒤,
`pip freeze >> requirements.txt`를 통해 사용한 라이브러리 list를 남겨준다.

설치 시에는 `pip install -r requirements.txt`를 통해 필요한 라이브러리를 설치해준다. (가상환경 사용 권장)

## modelForm을 통해 자동 생성된 Form 수정하기

`forms.py`의 class에 다음과 같은 코드를 추가하여 form을 수정할 수 있다. 
```python
class Meta:
        model = Article
        exclude = ('user',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }
```